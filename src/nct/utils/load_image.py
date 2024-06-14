import os
import subprocess
import shutil

def fetch_and_preproc_image_cGAN_NoSeg(path_in, tmpdir):
    '''
    :param path_in: Path to the input image
    :param tmpdir: Path to tempdirectory
    :return: out_decathlon_monai: list of dictionary with the preprocessed image path (like monai load_decathlon_datalist)
        [
            {'image': '/workspace/data/chest_19.nii.gz',
        ]
    '''
    # Check if paths exist
    path_in = os.path.abspath(path_in)
    if not os.path.exists(path_in):
        raise ValueError(f'Error with path: {path_in} does not exist')
    
    # Create temp_in and temp_seg
    temp_in_path = os.path.join(tmpdir, os.path.basename(path_in))
    shutil.copyfile(path_in, temp_in_path)
    return [{'image': temp_in_path}]
