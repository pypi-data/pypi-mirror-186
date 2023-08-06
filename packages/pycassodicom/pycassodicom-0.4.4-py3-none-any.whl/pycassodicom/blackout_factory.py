"""
Black-out Factory

Depending on Modality and Manufacturer, different amount of pixels must be blackend.
Also, the image size and photometric interpretation is different
for different manufacturers and modalities.
"""
from abc import ABC
from dataclasses import dataclass
import numpy as np
from pydicom import Dataset

from .update_dicom_tags import update_ds


@dataclass
class PhotometricInterpretation:
    dataset: Dataset

    def get_image(self):
        return self.dataset.pixel_array

    def write_dataset(self, img):
        self.dataset.PixelData = img
        return self.dataset
    
    def make_black(self, pixels):
        img = self.get_image()
        try:
            img[0:pixels-1, :, :] = 0
        except IndexError:
            img[0:pixels-1, :] = 0

        return self.write_dataset(img)


class YBRFull422(PhotometricInterpretation):
    def __int__(self, dataset):
        PhotometricInterpretation.__init__(dataset)

    def get_image(self):
        img = self.dataset.pixel_array
        try:
            img = np.repeat(img[:, :, :, 0, np.newaxis], 3, axis=3)
        except IndexError:
            img = np.repeat(img[:, :, 0, np.newaxis], 3, axis=2)

        return img

    def write_dataset(self, img):
        self.dataset.PixelData = img
        self.dataset.PhotometricInterpretation = 'RGB'
        return self.dataset

    def make_black(self, pixels):
        img = self.get_image()
        try:
            img[:, 0:pixels-1, :, :] = 0
        except IndexError:
            img[0:pixels-1, :, :] = 0

        return self.write_dataset(img)


class RGB(PhotometricInterpretation):
    def __int__(self, dataset):
        super().__init__(dataset)

    def make_black(self, pixels):
        img = self.get_image()
        try:
            img[:, 0:pixels-1, :, :] = 0
        except IndexError:
            try:
                img[0:pixels-1, :, :] = 0
            except IndexError:
                img[0:pixels-1, :] = 0

        return self.write_dataset(img)


class PaletteColor(PhotometricInterpretation):
    def __int__(self, dataset):
        super().__init__(dataset)

    def write_dataset(self, img):
        self.dataset.PixelData = img
        return self.dataset

    def make_black(self, pixels):
        img = self.get_image()
        try:
            img[:, 0:pixels-1, :] = 0
        except IndexError:
            img[0:pixels-1, :] = 0

        return self.write_dataset(img)


class MonoChrome2(PhotometricInterpretation):
    def __int__(self, dataset):
        super().__init__(dataset)

    def write_dataset(self, img):
        self.dataset.PixelData = img
        return self.dataset

    def make_black(self, pixels):
        img = self.get_image()
        try:
            img[:, 0:pixels-1, :] = 0
        except IndexError:
            img[0:pixels-1, :] = 0

        return self.write_dataset(img)


@dataclass
class Agfa:
    """Philips manufacturer"""
    dataset: Dataset

    def process_image(self):
        """Different process for different photometric interpretation and image size."""

        if self.dataset.PhotometricInterpretation == 'RGB':
            return update_ds(RGB(self.dataset).make_black(pixels=50))


@dataclass
class Philips:
    """Philips manufacturer"""
    dataset: Dataset

    def process_image(self):
        """Different process for different photometric interpretation and image size."""

        if self.dataset.PhotometricInterpretation == 'MONOCHROME2':
            return update_ds(MonoChrome2(self.dataset).make_black(pixels=60))

        if self.dataset.PhotometricInterpretation == 'YBR_FULL_422':
            return update_ds(YBRFull422(self.dataset).make_black(pixels=60))

        if self.dataset.PhotometricInterpretation == 'RGB':
            return update_ds(RGB(self.dataset).make_black(pixels=60))

        if self.dataset.PhotometricInterpretation == 'PALETTE COLOR':
            return update_ds(PaletteColor(self.dataset).make_black(pixels=60))


@dataclass
class Toshiba:
    """Toshiba manufacturer"""
    dataset: Dataset

    def process_image(self):
        """Different process for different photometric interpretation and image size."""
        if self.dataset.PhotometricInterpretation == 'RGB':
            return update_ds(RGB(self.dataset).make_black(pixels=50))

        if self.dataset.PhotometricInterpretation == 'YBR_FULL_422':
            return update_ds(YBRFull422(self.dataset).make_black(pixels=60))


@dataclass
class GeneralElectrics:
    """GE manufacturer"""
    dataset: Dataset

    def process_image(self):
        """Different process for different photometric interpretation and image size."""
        if self.dataset.PhotometricInterpretation == 'RGB':
            return update_ds(RGB(self.dataset).make_black(pixels=50))

        if self.dataset.PhotometricInterpretation == 'YBR_FULL_422':
            return update_ds(YBRFull422(self.dataset).make_black(pixels=50))


@dataclass
class Modality(ABC):
    dataset: Dataset

    def process_by_manufacturer(self):
        return self.dataset


class USModality(Modality):
    """US (ultra sound) modality"""
    def __int__(self, dataset):
        Modality.__init__(dataset)

    def process_by_manufacturer(self):
        """Different manufacturers need different process."""
        if str(self.dataset.Manufacturer).lower().find('philips') > -1:
            return Philips(self.dataset).process_image()

        if str(self.dataset.Manufacturer).lower().find('toshiba') > -1:
            return Toshiba(self.dataset).process_image()

        if str(self.dataset.Manufacturer).find('GE') > -1:
            return GeneralElectrics(self.dataset).process_image()

        return self.dataset


class MRModality(Modality):
    """MR (magnet resonance tomography) modality"""
    def __int__(self, dataset):
        super().__init__(dataset)


class CTModality(Modality):
    """CT (computed tomography) modality"""
    def __int__(self, dataset):
        super().__init__(dataset)

    def process_by_manufacturer(self):
        """Different manufacturers need different process."""
        if str(self.dataset.Manufacturer).lower().find('agfa') > -1:
            return Agfa(self.dataset).process_image()


class CRModality(Modality):
    """CR (computed radiology) modality"""

    def __int__(self, dataset):
        super().__init__(dataset)


def blackout(dataset):
    """
    Different modalities need different processes.
    SOPClassUID is more exact.
    """
    sop_class = str(dataset.SOPClassUID)

    if sop_class.find('1.2.840.10008.5.1.4.1.1.3.1') == 0:
        return USModality(dataset).process_by_manufacturer()

    if sop_class.find('1.2.840.10008.5.1.4.1.1.4') == 0:
        return MRModality(dataset).process_by_manufacturer()

    if sop_class.find('1.2.840.10008.5.1.4.1.1.2') == 0:
        return CTModality(dataset).process_by_manufacturer()

    # TODO: include other modalities or rather SOPClassUIDs!
    if dataset.Modality == 'CR':
        return CRModality(dataset).process_by_manufacturer()

    return dataset
