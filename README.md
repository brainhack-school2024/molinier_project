# About me

<a href="https://github.com/NathanMolinier">
   <img src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/35bf52a6-ed2a-4c7f-944f-a040242f5154" width="100px;" alt=""/>
</a>

My name is Nathan Molinier, I'm a PhD student at Polytechnique Montreal, and I use deep learning methods to identify spinal structures on MRI scans.

# My brainhack project
## Tools
For this project, I used:
- `git` and `github` for versioning
- `python` to train and evaluate my deep learning approach
## Context

Unlike other non-invasive medical imaging techniques such as computed tomography (CT scans), X-rays, or ultrasounds, Magnetic Resonance Imaging (MRI) employs various protocols resulting in significantly distinct images, also referred to as contrasts. While these contrasts are valuable in medical diagnosis for facilitating tissue identification and characterizing pathologies, they pose numerous challenges when it comes to the utilization of automated methods such as deep learning. Depending on the selected imaging parameters, there can be significant variations in intensity and noise distributions for the same region of interest, greatly impacting the capability and robustness of automated methods. Although significant efforts are currently being made to address this limitation by training models on a wider range of contrasts, many of single contrasts approaches remain underutilized due to a lack of compatibility between the training data and the data available for testing the models. To mitigate this issue, we propose converting any contrast into a simulated T2-weighted (T2w) image, which could be used to leverage the performance of deep learning models specifically trained on T2w contrasts. Given the complexity of accessing multi-contrast data, the aim of this initiative is to extend the scope of deep learning work regardless of the number of contrasts used for training.

### Examples

These deep learning models were only trained on T2-weighted scans

| Spine segmentation | Spinal cord segmentation |
|:---:|:---:|
| <img width="682" alt="Screenshot 2024-06-14 at 09 41 57" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/9f92316a-3c05-441b-9315-6c2517ab0bc2"> | <img width="637" alt="Screenshot 2024-06-14 at 09 42 22" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/0c4bfbef-8910-4881-baef-aeb1464d1a01"> |

## Contrast translation approach

My objective was to generate fake T2w scans from any given contrast to lure deep learning models that were only trained on T2w scans during inference.

### Datasets

| Dataset name | Subjects | Contrasts used | Open source | Link |
| :---: | :---: | :---: | :---: | :---: |
| spine generic | 267 | T1w and T2w | yes | https://github.com/spine-generic/data-multi-subject |
| canproco | 450 | PSIR, STIR and T2w | No | X |
| lumbar-nusantara | 515 | T1w and T2w | yes | https://data.mendeley.com/datasets/k57fr854j2/2 |
| spider | 218 | T1w and T2w | yes | https://spider.grand-challenge.org/ |

### Preprocessing steps and method

<img width="1123" alt="Screenshot 2024-06-14 at 09 53 12" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/a8c90f38-be21-435f-8f55-8bebaffb5395">

### Previous work on cervical FOV

For this work, the datasets `spine-generic` and `canproco` were used for the training of the cGAN approach.

<img width="1123" alt="Screenshot 2024-06-14 at 09 55 18" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/17379015-3f07-4542-96f6-d97a899f6ab4">

> spineps: https://github.com/Hendrik-code/spineps

### Extension of the method for lumbar FOV

For this work, the dataset `spider` was used for inference, the cGAN approach was only trained with the dataset `lumbar-nusantara`.

<img width="1123" alt="Screenshot 2024-06-14 at 13 52 30" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/40ff2c71-5454-4fcc-8f6f-82bca7b61e06">

> Surprisingly [spineps](https://github.com/Hendrik-code/spineps) performed well on the T1w lumbar scans of the `spider` dataset. One possible reason is that spineps was actually trained on the T2w scans of the same patients in this dataset.

### Evaluation of the lumbar spine segmentations

To evaluate the quality of the final segmentations with and without the use of the contrast translation approach, the framework [panoptica](https://github.com/BrainLesion/panoptica) was used.

> panoptica allows us to evaluate segmentations from both semantic and instance standpoint ([paper](https://arxiv.org/abs/2312.02608))

#### Global metrics

Here, segmentations are binarized and metrics are computed on the full segmentations.

| Global Dice Score | Global average symmetric surface distance (ASSD)|
| :---: | :---: |
| <img width="645" alt="Screenshot 2024-06-14 at 14 12 28" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/0d523670-408b-48fd-9557-522369497605"> | <img width="779" alt="Screenshot 2024-06-14 at 14 14 17" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/6eb20996-362d-415b-acaf-dbb3aff115fe"> |
| <img width="850" alt="Screenshot 2024-06-14 at 14 12 28" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/dbd71b84-bda4-437c-9f2f-3c1a2b96c6cd"> | <img width="800" alt="Screenshot 2024-06-14 at 14 12 28" src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/21c0327a-2b47-44b8-88e4-b8accb3835df"> |

#### Instance wise metrics

Here, segmentations were aligned by panoptica and metrics were computed for each instance (individual vertebrae/discs). The mean and standard deviation is then plotted.

| Instance Dice Score | Instance average symmetric surface distance (ASSD)| Instance intersection over union (IoU) |
| :---: | :---: | :---: |
| ![instance_dice](https://github.com/brainhack-school2024/molinier_project/assets/68945192/e97f448b-2ca8-4ba3-8f50-f62bde29bec4) | ![instance_assd](https://github.com/brainhack-school2024/molinier_project/assets/68945192/567edb86-43da-4ffc-8dc5-68770cd4b196) | ![instance_iou](https://github.com/brainhack-school2024/molinier_project/assets/68945192/0b25f2a5-bb12-4c5c-9dc8-09ae678256c1) |
|![instance_dice_std](https://github.com/brainhack-school2024/molinier_project/assets/68945192/ecdb579c-5f8f-418e-8849-88c57b9e996f) | ![instance_assd_std](https://github.com/brainhack-school2024/molinier_project/assets/68945192/866f0c5f-3eb4-4659-b01f-34db018c0e44) | ![instance_iou_std](https://github.com/brainhack-school2024/molinier_project/assets/68945192/f17a912c-c56e-4f38-8ca7-5fea216e614f) |

| False negative detections (FN) | False positive detections (FN) |
| :---: | :---: |
|![false_negative](https://github.com/brainhack-school2024/molinier_project/assets/68945192/94afdc12-0281-49c4-ac34-f4cc638cf79c) | ![false_positive](https://github.com/brainhack-school2024/molinier_project/assets/68945192/20ea3f4f-aacd-4719-9bb3-cee66bb9e56b)|

### Discussion

- One possible reason why spineps worked on a T1w image is that the network was actually trained on the T2w images of the same subjects in the dataset `spider`
- The increasing rate of false detections (FP and FN) is probably due to the fact that the same features and properties do not appear is the input and output contrast of the translation algorithm: therefore during its training the cGAN may have learned to invent some structures that were not present.
- The reduction of the dice score and the augmentation of the ASSD metrics is also probably due to slight shape differences of the spine between the input and output contrast.

### Conclusion

Using a contrast translation approach is relevant only if the model does not perform well on the input contrast. Because a naive translation between two different contrasts may lead to slight modifications of the anatomy.

To validate the translation approach with vertebral labeling, the inference should be done on a different dataset which was not seen during training of the two deep learning models. Currently, too few MRI datasets with manual segmentation of the spine are available open-source.

### References

- Isola, Phillip, Jun-Yan Zhu, Tinghui Zhou, and Alexei A. Efros. “Image-To-Image Translation With Conditional Adversarial Networks,” 1125–34, 2017. https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html.
  
- Graf, Robert, Joachim Schmitt, Sarah Schlaeger, Hendrik Kristian Möller, Vasiliki Sideri-Lampretsa, Anjany Sekuboyina, Sandro Manuel Krieg, et al. “Denoising Diffusion-Based MRI to CT Image Translation Enables Automated Spinal Segmentation.” European Radiology Experimental 7, no. 1 (November 14, 2023): 70. https://doi.org/10.1186/s41747-023-00385-2.
  
- Möller, Hendrik, Robert Graf, Joachim Schmitt, Benjamin Keinert, Matan Atad, Anjany Sekuboyina, Felix Streckenbach, et al. “SPINEPS -- Automatic Whole Spine Segmentation of T2-Weighted MR Images Using a Two-Phase Approach to Multi-Class Semantic and Instance Segmentation.” arXiv, February 26, 2024. http://arxiv.org/abs/2402.16368.
  
- Kofler, Florian, Hendrik Möller, Josef A. Buchner, Ezequiel de la Rosa, Ivan Ezhov, Marcel Rosier, Isra Mekki, et al. “Panoptica -- Instance-Wise Evaluation of 3D Semantic and Instance Segmentation Maps.” arXiv, December 5, 2023. https://doi.org/10.48550/arXiv.2312.02608.


# Installation

The following steps are describing how to run the inference of the contrast-translation approach.

> More information about the training will be described in this [repository](https://github.com/spinalcordtoolbox/disc-labeling-playground)

1. First, create a conda environment with python 3.10.

```bash
conda create --name nct-env python=3.10
conda activate nct-env
conda install pip
```

2. Install the correct version of [pytorch](https://pytorch.org/get-started/locally/) in you environment.

3. Clone this repository
```bash
git clone git@github.com:brainhack-school2024/naive-mri-contrast-translation.git
```

4. Install the package and the requirements
```bash
cd naive-mri-contrast-translation
pip install -r requirements.txt
pip install -e .
```

5. Download the network weights from the release

# Usage

Generate a fake T2w scans from an input contrast 

```
python src/nct/inference/run_cgan_inference.py --path-in IMG_PATH --path-out OUT_PATH --weight-path WEIGHTS
```

With:
- `IMG_PATH` corresponding to the path to your input image
- `OUT_PATH` corresponding to the discs labels output path
- `WEIGHTS` corresponding to the path to the network weights from the release


