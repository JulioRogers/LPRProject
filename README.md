
# LPRProject
A Computer Vision Project about License Plates Recognition.


## Description
This is a project that is based on detecting car license plates using an AI, from video recording on a surviliance scenario.

<!--## Getting Started

Steps to generate the dataset:

1. Download a video in which you can see cars with their respective plates.
2. Generate video frames.
3. Use the web application https://cloud.annotations.ai/ to start labeling.


   3.1. Select the type of annotator "Location".


   3.2. Locate the cars and their respective plates.


   3.3. Export the result file.


4. Excecute the labeler.py:
```bash
python labeler.py --path _anotations.json
```
-->

## Dataset

The primary sequence to describe the data preparing process of the license plate recognition system will be:

1. Record videos from natural sceneries <br/>

The videos that are used for the training process were taken from a surveillance scenario. It was from a camera in Malteria shopping center, Latacunga - Ecuador. In this case, we record three different videos of one hour with a frame rate of 20 fps and with a size of 1920x1080. The two first videos were used for training and valuation. The last one was edited to have a permanent flow of cars and used for inference.

2. Divide the obtained videos into frames <br/>

The videos used for training and valuation were cropped by frames using a python script that automatically makes this process. On average, we get 12 000 crops for each video, and only 3400 were valid images for making annotations from these crops.

3. Localize car and plate <br/>

The objective of make crops from each video was to make localization of plates and cars using bounding boxes on each video crop. To gain it, we use [IMB cloud annotations]([https://cloud.annotations.ai](https://cloud.annotations.ai/)), an open-source image annotation tool where you can quickly build real-time object detection models without code. The IMB tool gives different options to export the annotations after detecting the elements at the cropped image. In this case, we exported as YOLO.

4. According to the annotations, make a plate crop. <br/>

We make another python script, "crop_plate.py" that crops the plate from the images using the coordinates from the YOLO annotations. After making the crops, we proceeded to label the plates with their transcription using an event app called [labelerJS]([https://github.com/Tubaher/labelerJS](https://github.com/Tubaher/labelerJS)). After cropping the plates, the images are used to be in different sizes. At this point, it is crucial to make a resize using the python script "[resize.py](http://resize.py/)". In this case, we resize the images to 96x48 because this is the size that our secondary classifier (LPRnet) requires as training input. After labeling, we obtain 590 plate labeled images, where 560 were for training and 30 for valuation.

5. Images and bounding boxes resize <br/>

The Primary Detector takes as an input a specific size of the image. That is why it is necessary to resize the annotated images and their bounding boxes using the python script "resize_bbox.py". For this step is necessary to download the standard zip format from IBM cloud annotations.

## Model training 

Our work focuses on the maximum performance of the ALPR system in an urban scenario. Then, we have to replace the approach of 3 cascaded models to reach the license plate characters for a two-step system. We employ a primary detector for cars and plates and a secondary classifier for character recognition in the LPs. Across this section will describe the process we made for training and prepare the two different models.

### Primary detector 

Our primary detector module is prepared for car and plates detection. The architecture selected was DetectNet_v2 which employs a ResNet-10 as its backbone. The detectnet V2 is an Nvidia Object detection model whose principal features use two-loss functions to predict object coverage and object bounding box. Then, a clustering module produces the final set of bounding boxes. The model uses the mean average precision (mAP) metric to evaluate the validation dataset DetectNet_v2 can perform feature extraction with different networks as the backbone. However, for the best trade between precision and performance, we employed ResNet 10.

### Secondary Classifier 
For the character recognition task, we implemented a version of LPRNet, where we took the basis for Chinese and USA license plates to prepare our module over Ecuadorian license plates. For training the LPRNet, we created a different checkpoint after adding each dataset. Therefore, we first focus on having a solid feature extraction for character recognition, and then we specialized the classification layers for the different surveillance scenarios.

## Authors: 
Diego Suntaxi - [@tubaher](https://github.com/Tubaher) <br/>
Samantha Quintanchala - [@samanthacqs](https://github.com/samanthacqs) <br/>
Julio Cajas - [@JulioRogers](https://github.com/JulioRogers) <br/>
