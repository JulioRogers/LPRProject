import os
from PIL import Image


filesPath = 'gama/gama-5' #input files path
files = os.listdir(filesPath)
desPath = 'gama/cropped' #output files path



def istxt(file): 
    if file[-4:] == '.txt':
        return True
    else:
        return False


# def isjpg(file):
#     if file[-4:] == '.jpg':
#         return True
#     else:
#         return False


def bbox(x, y, w, h): 
    left = (x*1500)-((w*1500)/2)
    top = (y*843)-((h*843)/2)
    right = (x*1500)+((w*1500)/2)
    bottom = (y*843)+((h*843)/2)


    return left, top, right, bottom


annot = filter(istxt, files)
# image = filter(isjpg, files)

listannot = list(annot)

# print(listannot)

for annotation in listannot:
	base1 = os.path.basename(annotation)
	base = base1[:-4]
	plates = []
	with open(os.path.join(filesPath, annotation)) as f:
		lines = f.readlines()
		# print(lines)
		for line in lines:
			if line[0] == '1': #the number depends on the plate class 
				if '\n' in line:
					line = line[:-1]
				plates.append(line.split())
	
	cont=0

	for plate in plates:
		print(float(plate[1]), float(plate[2]), float(plate[3]), float(plate[4]), '--', base)
		left, top, right, bottom = bbox(float(plate[1]), float(plate[2]), float(plate[3]), float(plate[4]))
		# print(left, top, right, bottom)
		im = Image.open(os.path.join(filesPath,base+'.jpg')).convert('L')
		im = im.crop((left, top, right, bottom))
		im.save(os.path.join(desPath,base+'_'+str(cont)+'.jpg'))
		cont+=1



