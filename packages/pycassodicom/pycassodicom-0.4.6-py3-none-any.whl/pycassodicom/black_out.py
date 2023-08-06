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
    sop_class = dataset.SOPClassUID
    modality = dataset.Modality
    try:
        if 'INVALID' in (x for x in dataset.ImageType):
            return True

        if modality == 'US' and \
                (dataset.NumberOfFrames is None or sop_class.find('1.2.840.10008.5.1.4.1.1.3.1') == -1):
            return True

        if sop_class == '1.2.840.10008.5.1.4.1.1.7':
            return True

        if dataset.Modality == 'MR' and sop_class.find('1.2.840.10008.5.1.4.1.1.4') == -1:
            return True

        if dataset.Modality == 'CT' and sop_class.find('1.2.840.10008.5.1.4.1.1.2') == -1:
            return True

        return False

    except AttributeError:
        return False
