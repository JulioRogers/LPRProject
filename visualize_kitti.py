import argparse
import logging
import cv2 as cv

parser = argparse.ArgumentParser(description='Visualize kitti annotations')
parser.add_argument('--ann',  type=str, required=True, help='Path to kitti annotations file')
parser.add_argument('--img',  type=str, required=True, help='Path to image')

# Level of warnings
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.INFO) 


def read_kitti(path):
    bboxk = []
    with open(path, "r") as f:
        objects = f.readlines()
        for annotation in objects:
            annotation = annotation.split()
            print(annotation)
            start_point = (int(float(annotation[4])), int(float(annotation[5])))
            end_point = (int(float(annotation[6])), int(float(annotation[7])))
            bboxk.append((start_point, end_point))

    return bboxk


def plot_kitti(img,bboxk, color=(255, 0, 0), thickness=2):
    
    for bbox in bboxk:
        print(bbox[0], bbox[1])
        cv.rectangle(img, bbox[0], bbox[1], color, thickness= thickness)


def main():
    global args
    args = parser.parse_args()
    ann = args.ann
    img = args.img

    im = cv.imread(img)
    bboxk = read_kitti(ann)
    plot_kitti(im, bboxk)

    cv.imwrite('vis.jpg',im)

if __name__ == '__main__':
    main()
