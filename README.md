
# LPRProject
A Computer Vision Project about License Plates Recognition.


## Description
This is a project that is based on detecting car license plates using an AI, from video recording on a surviliance scenario.

## Getting Started

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


## Authors: 
Diego Suntaxi - [@tubaher](https://github.com/Tubaher) <br/>
Samantha Quintanchala - [@samanthacqs](https://github.com/samanthacqs) <br/>
Julio Cajas - [@JulioRogers](https://github.com/JulioRogers) <br/>
