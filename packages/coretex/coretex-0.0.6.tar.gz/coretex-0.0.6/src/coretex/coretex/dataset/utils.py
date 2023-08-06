import logging

from .dataset import Dataset


def downloadDataset(dataset: Dataset) -> None:
    # TODO: Should we think about using deprecation package for handling this?
    logging.warning(">> [Coretex] (downloadDataset) function is deprecated use Dataset.download instead")

    dataset.download()
