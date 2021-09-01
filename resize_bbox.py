import argparse
import numpy as np
import cv2
import os
# from PIL import Image
parser = argparse.ArgumentParser(description='Values for image resize')
parser.add_argument('--width',  type=str, required=True, help='width value')
parser.add_argument('--height',  type=str, required=True, help='height value')
# parser.add_argument('--imagePath',  type=str, required=True, help='image path')
# parser.add_argument('--annotPath',  type=str, required=True, help='Kitti annotation path')


# desPath = '/home/ubuntu/LPRProject/car_plate_final'
desPathim = '/home/ubuntu/LPRProject/car_plate_final/images_resized' #output files path
desPathan = '/home/ubuntu/LPRProject/car_plate_final/labels_resized'

args = parser.parse_args()
width_n = int(args.width)
height_n = int(args.height)
# imagePath = args.magePath
# annotPath = args.annotPath

imagePath = '/home/ubuntu/LPRProject/car_plate_final/images'
annotPath = '/home/ubuntu/LPRProject/car_plate_final/labels'

annots = os.listdir(annotPath) #annotations list
images = os.listdir(imagePath) #imagees list

for image in images:
    namei=image[:-4]
    img = cv2.imread(os.path.join(imagePath,image))
    print(os.path.join(imagePath,image),'---done')
    height = np.size(img, 0)
    width = np.size(img, 1)
    newImg = cv2.resize(img, (width_n, height_n))
    cv2.imwrite(os.path.join(desPathim,namei+'_resize.jpg'), newImg)
    

    objects = []
    with open(os.path.join(annotPath, namei+'.txt')) as f:
        lines = f.readlines()
		    # print(lines)
        for line in lines:
            if '\n' in line:
                line = line[:-1]
            objects.append(line.split())
    # print(objects)
    
    for object in objects:
        object[4]=str(round((float(object[4])/width)*width_n,2))
        object[5]=str(round((float(object[5])/height)*height_n,2))
        object[6]=str(round((float(object[6])/width)*width_n,2))
        object[7]=str(round((float(object[7])/height)*height_n,2))
        object[-1]=object[-1]+'\n'


    with open(os.path.join(desPathan, namei+'_resize.txt'), 'w') as f1:
        for obj in objects:
            f1.write(' '.join(obj))
            
            print(os.path.join(annotPath,image),'---done')

   
        



    

        

