from typing import Any, Optional, Tuple

from pathlib import Path
from zipfile import ZipFile

import os
import logging
import shutil
import pickle
import hashlib
import zipfile

import requests

from ..folder_management import FolderManager


IGNORED_FILE_TYPES = [".pt"]


class CacheException(Exception):
    pass


def __hashedKey(key: str) -> str:
    return hashlib.sha256(key.encode("UTF-8")).hexdigest()


def __zip(zipPath: Path, filePath: Path, fileName: str) -> None:
    baseName, fileExtension = os.path.splitext(filePath)

    if fileExtension in IGNORED_FILE_TYPES or not zipfile.is_zipfile(filePath):
        with ZipFile(zipPath, mode = "w") as archive:
            archive.write(filePath, fileName)

        filePath.unlink(missing_ok = True)
    else:
        filePath.rename(FolderManager.instance().cache / filePath.name)


def downloadFromUrl(url: str, fileName: str) -> Tuple[Path, str]:
    tempPath = FolderManager.instance().temp
    hashUrl = __hashedKey(url)
    fileName, fileExtension = os.path.splitext(fileName)

    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        resultPath = os.path.join(tempPath, hashUrl)
        fileName = f"{hashUrl}{fileExtension}"
        resultPath = os.path.join(tempPath, fileName)

        with open(resultPath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    return Path(resultPath), fileName


def storeObject(key: str, object: Any, override: bool = False) -> None:
    hashedKey = __hashedKey(key)
    zipPath = (FolderManager.instance().cache / hashedKey).with_suffix(".zip")

    pickleName = f"{hashedKey}.pickle"
    picklePath = FolderManager.instance().cache / pickleName

    if override:
        zipPath.unlink(missing_ok = True)
        logging.info(">> [Coretex] Overriding existing cache.")

    if not override and picklePath.exists():
        raise CacheException(">> [Coretex] Cache with given key already exists. Set parameter override to True if you wanna override existing cache.")

    with open(picklePath, "wb") as pickleFile:
        pickle.dump(object, pickleFile)

    __zip(zipPath, picklePath, pickleName)


def storeFile(key: str, filePath: str, override: bool = False) -> None:
    hashedKey = __hashedKey(key)
    cachePath = FolderManager.instance().cache / hashedKey
    cacheZipPath = cachePath.with_suffix(".zip")

    if override:
        cacheZipPath.unlink(missing_ok = True)
        logging.info(">> [Coretex] Overriding existing cache.")

    if not override and cacheZipPath.exists():
        raise CacheException(">> [Coretex] Cache with given key already exists. Set parameter override to True if you wanna override existing cache.")

    logging.info(">> [Coretex] Cache with given key doesn't exist, caching...")
    shutil.copy(filePath, cachePath)

    __zip(cacheZipPath, cachePath, hashedKey)


def storeUrl(url: str, fileName: str, override: bool = False) -> None:
    hashedKey = __hashedKey(url)
    cacheZipPath = (FolderManager.instance().cache / hashedKey).with_suffix(".zip")

    if override:
        cacheZipPath.unlink(missing_ok = True)
        logging.info(">> [Coretex] Overriding existing cache.")

    if not override and cacheZipPath.exists():
        raise CacheException(">> [Coretex] Cache with given key already exists. Set parameter override to True if you wanna override existing cache.")

    logging.info(f">> [Coretex] Caching file from {url}.")

    resultPath, fileName = downloadFromUrl(url, fileName)

    __zip(cacheZipPath, resultPath, fileName)

    logging.info(f">> [Coretex] File cached successfully.")


def load(key: str) -> Any:
    hashedKey = __hashedKey(key)
    cacheZipPath = (FolderManager.instance().cache / hashedKey).with_suffix(".zip")
    picklePath = (FolderManager.instance().cache / hashedKey).with_suffix(".pickle")

    if not cacheZipPath.exists():
        raise CacheException(">> [Coretex] Cache with given key doesn't exist.")

    with ZipFile(cacheZipPath, "r") as zipFile:
        zipFile.extractall(FolderManager.instance().cache)

        logging.info(">> [Coretex] Cache with given key exists, loading cache...")

        with open((picklePath), "rb") as pickleFile:
            loadedPickle = pickle.load(pickleFile)

    return loadedPickle


def getPath(key: str) -> Optional[Path]:
    hashedKey = __hashedKey(key)
    cacheZipPath = (FolderManager.instance().cache / hashedKey).with_suffix(".zip")

    if not cacheZipPath.exists():
        raise CacheException(">> [Coretex] Cache with given key doesn't exist.")

    return cacheZipPath


def exists(key: str) -> bool:
    hashedKey = __hashedKey(key)
    cacheZipPath = (FolderManager.instance().cache / hashedKey).with_suffix(".zip")

    return cacheZipPath.exists()


def remove(key: str) -> None:
    hashedKey = __hashedKey(key)
    cacheZipPath = (FolderManager.instance().cache / hashedKey).with_suffix(".zip")

    if not cacheZipPath.exists():
        raise CacheException(">> [Coretex] Cache with given key doesn't exist.")

    logging.info(">> [Coretex] Cache with given key exists, removing cache...")
    cacheZipPath.unlink(missing_ok = True)


def clear() -> None:
    shutil.rmtree(FolderManager.instance().cache)
