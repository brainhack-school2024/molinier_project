# Short biography

<a href="https://github.com/NathanMolinier">
   <img src="https://github.com/brainhack-school2024/molinier_project/assets/68945192/35bf52a6-ed2a-4c7f-944f-a040242f5154" width="15px;" alt=""/>
</a>

My name is Nathan Molinier, I'm a PhD student at Polytechnique Montreal, and I use deep learning methods to identify spinal structures on MRI scans.

# My brainhack project
## Context

Unlike other non-invasive medical imaging techniques such as computed tomography (CT scans), X-rays, or ultrasounds, Magnetic Resonance Imaging (MRI) employs various protocols resulting in significantly distinct images, also referred to as contrasts. While these contrasts are valuable in medical diagnosis for facilitating tissue identification and characterizing pathologies, they pose numerous challenges when it comes to the utilization of automated methods such as deep learning. Depending on the selected imaging parameters, there can be significant variations in intensity and noise distributions for the same region of interest, greatly impacting the capability and robustness of automated methods. Although significant efforts are currently being made to address this limitation by training models on a wider range of contrasts, many of single contrasts approaches remain underutilized due to a lack of compatibility between the training data and the data available for testing the models. To mitigate this issue, we propose converting any contrast into a simulated T2-weighted (T2w) image, which could be used to leverage the performance of deep learning models specifically trained on T2w contrasts. Given the complexity of accessing multi-contrast data, the aim of this initiative is to extend the scope of deep learning work regardless of the number of contrasts used for training.

## Previous work

