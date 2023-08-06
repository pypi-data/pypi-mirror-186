"""
Update DICOM Tags

"""
from pydicom import Dataset
from pydicom.uid import ExplicitVRLittleEndian


def update_ds(dataset: Dataset) -> Dataset:
    """
    Since the image is changed, the dicom tags have to change, too.
    - no burned-in anymore
    - transfer syntax changes, too
    - add, which method was used
    """
    dataset.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian
    dataset.BurnedInAnnotation = 'NO'
    dataset.PatientIdentityRemoved = 'YES'

    ds_sq = Dataset()
    ds_sq.CodeValue = '113101'
    dataset.DeidentificationMethodCodeSequence.append(ds_sq)
    return dataset
