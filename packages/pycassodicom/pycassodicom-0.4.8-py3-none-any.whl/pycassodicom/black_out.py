"""
PycassoDicom

Script for de-identifying images with burned in annotation.
Depending on manufacturer and image size, pixel can be blackened.
Some images are of no use for the researcher or have too much identifying information.
They will be deleted (set to None).
"""
from pydicom import Dataset

from .blackout_factory import blackout


def blacken_pixels(dataset: Dataset) -> Dataset:
    """
    Blacken pixel based on manufacturer, modality and image size.

    You can filter out all the secondary image types already in this step.
    """
    try:
        if 'PRIMARY' in (x for x in dataset.ImageType):
            return blackout(dataset)

        return dataset

    except AttributeError:
        return dataset


def delete_dicom(dataset: Dataset) -> bool:
    """
    True if the dicom can be deleted.
    """
    try:
        sop_class = dataset.SOPClassUID
        modality = dataset.Modality

        if modality == 'US' \
                and dataset.NumberOfFrames is not None \
                and '1.2.840.10008.5.1.4.1.1.3.1' in sop_class:
            return False

        if modality == 'MR' and '1.2.840.10008.5.1.4.1.1.4' in sop_class:
            return False

        if modality == 'CT' and '1.2.840.10008.5.1.4.1.1.2' in sop_class:
            return False

        return True

    except AttributeError:
        return True
