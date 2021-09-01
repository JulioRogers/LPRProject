import argparse
import cv2
import os
parser = argparse.ArgumentParser(description='Values for image resize')
parser.add_argument('--width',  type=str, required=True, help='width value')
parser.add_argument('--height',  type=str, required=True, help='height value')

imagesPath='gama/cropped/'
images=os.listdir(imagesPath)

destPath="gama/cropped_r/"
print(images)

global args
args = parser.parse_args()
width = int(args.width)
height = int(args.height)


for image in images:
    name=image[:-4]

    img = cv2.imread(os.path.join(imagesPath,image))

    newImg = cv2.resize(img, (width, height))

    cv2.imwrite(os.path.join(destPath,name+'.jpg'), newImg)
