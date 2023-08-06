from typing import Generator, Optional
from pathlib import Path
from zipfile import ZipFile

import mimetypes
import zipfile
import tarfile
import gzip
import shutil
import logging


class InvalidFileExtension(Exception):
    pass


def guessMimeType(filePath: str) -> str:
    mimeTypesResult = mimetypes.guess_type(filePath)

    mimeType = mimeTypesResult[0]
    if mimeType is None:
        raise InvalidFileExtension

    return mimeType


def isGzip(path: Path) -> bool:
    # .gz compressed files always start with 2 bytes: 0x1F and 0x8B
    # Testing for this is not 100% reliable, it is highly unlikely
    # that "ordinary text files" start with those two bytes—in UTF-8 it's not even legal.
    # That's why we check for extension and do the byte checking
    # Ref: https://stackoverflow.com/a/3703300/7585106

    if not path.is_file():
        return False

    with open(path, 'rb') as file:
        return file.read(2) == b'\x1f\x8b' and path.name.endswith(".gz")


def isArchive(path: Path) -> bool:
    return zipfile.is_zipfile(path) or tarfile.is_tarfile(path)


def gzipDecompress(source: Path, destination: Path) -> None:
    if not isGzip(source):
        raise ValueError(">> [Coretex] Not a .gz file")

    with gzip.open(source, "r") as gzipFile, open(destination, "wb") as destinationFile:
        shutil.copyfileobj(gzipFile, destinationFile)


def walk(path: Path) -> Generator[Path, None, None]:
    for p in Path(path).iterdir(): 
        if p.is_dir(): 
            yield from walk(p)
            continue

        yield p.resolve()


def recursiveUnzip(entryPoint: Path, destination: Optional[Path] = None, remove: bool = False) -> None:
    logging.debug(f">> [Coretex] recursiveUnzip: source = {str(entryPoint)}, destination = {str(destination)}")

    if destination is None:
        destination = entryPoint.parent / entryPoint.stem

    # Decompress with gzip if is gzip
    if isGzip(entryPoint):
        gzipDecompress(entryPoint, destination)

        if remove:
            entryPoint.unlink()

        if not isArchive(destination):
            return

        # gzip nameing convention is .original_file_ext.gz, so by calling .stem we remove .gz
        # for destination
        recursiveUnzip(destination, destination.parent / destination.stem, remove = True)
        return

    if not isArchive(entryPoint):
        raise ValueError(">> [Coretex] Not an archive")

    if zipfile.is_zipfile(entryPoint):
        with ZipFile(entryPoint, "r") as zipFile:
            zipFile.extractall(destination)

    if tarfile.is_tarfile(entryPoint):
        with tarfile.open(entryPoint, "r") as tarFile:
            tarFile.extractall(destination)

    if remove:
        entryPoint.unlink()

    for path in walk(destination):
        if isArchive(path) or isGzip(path):
            recursiveUnzip(path, remove = True)
