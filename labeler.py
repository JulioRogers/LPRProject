import argparse
import json
import logging
import os
import shutil

#Create an Argument Parser Object to receive arguments
parser = argparse.ArgumentParser(description='Image relocator')
#Add information about the program argument
parser.add_argument('--path',  type=str, required=True, help='Path to JSON file')

# Level of warnings
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.INFO) 

""""Converting the information into a particular kind of format string"""
def string(label,x,y,x2,y2):
    return "{} 0.00 0 0.00 {} {} {} {} 0.00 0.00 0.00 0.00 0.00 0.00 0.00\n".format(label,round(x,2),round(y,2),round(x2,2),round(y2,2))

"""Creating a txt file using the same name of the image file."""
def create_label(fileName, list):
    labelName = fileName.split('.')[0]+'.txt'
    file = open(labelName, 'w')
    for el in list:
        #calling the string function and giving the information inside the list of the image features.
        file.write(string(el['label'], el['x'],el['y'],el['x2'],el['y2']))
    file.close
    return labelName



"""Function to sort images and labels by directories 
using the '_annotations.txt' file given by the software cloud.annotations.ai. """
def image_relocator(path):
    #Read the file '_annotations' which is given by the software cloud.annotations.ai
    with open(path) as json_file:
        data = json.load(json_file)
        #Create the directories labels and images
        try: 
            os.mkdir('labels')
        except:
            pass
        try: 
           os.mkdir('images')
        except:
            pass

        cont_err = 0
        
        '''Take the information of the argument 'annotations' from the '_annotations' file.
        The 'key' variable will be the name of the image file. 
        The 'value' variable will be a list of information about the image file.'''
        
        for key,value in data['annotations'].items():
            #Save the directories path in variables.
            target = os.path.join('images','')        #$$$$$$ Why inside the for loop???
            labelPath = os.path.join('labels','') 

            """Calling for the create_label which will return a txt file."""
            namelabel = create_label(key, value)

            try:
              """Saving the image in the images directory and the label in the labels directory """
              shutil.copy(key,target)
              shutil.move(namelabel,labelPath)
            except:
              cont_err += 1 
              pass
            
        print('type: ', type(data['annotations']))
        print(f'No se encontraron {cont_err} imagenes')
def main():
    global args
    args = parser.parse_args()
    path = args.path
    image_relocator(path)

if __name__ == '__main__':
    main()
