import argparse
import json
import logging
import os
import shutil

parser = argparse.ArgumentParser(description='Image relocator')
parser.add_argument('--path',  type=str, required=True, help='Path to JSON file')

# Level of warnings
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.INFO) 

def string(label,x,y,x2,y2):
    return "{} 0.00 0 0.00 {} {} {} {} 0.00 0.00 0.00 0.00 0.00 0.00 0.00\n".format(label,round(x,2),round(y,2),round(x2,2),round(y2,2))

def create_label(fileName, list):
    labelName = fileName.split('.')[0]+'.txt'
    file = open(labelName, 'w')
    for el in list:
        file.write(string(el['label'], el['x'],el['y'],el['x2'],el['y2']))
    file.close
    return labelName



def image_relocator(path):
    with open(path) as json_file:
        data = json.load(json_file)
        try: 
            os.mkdir('labels')
            os.mkdir('images')
        except:
            pass
        try: 
            os.mkdir('images')
        except:
            pass
        #print(data)
        #Create a folder for each label
        # for label in data['labels']:
        #   cont_err = 0
        #   try:
        #     os.mkdir(label)
        #   except:
        #     pass
        cont_err = 0
        for key,value in data['annotations'].items():
            #print("key: {}, value: {} ".format(key, data) )
            #path, file_name = os.path.split(key)
            #target = os.path.join(value[0]['label'],key) anterior
            # path a donde se va a copiar
            target = os.path.join('images','')
            labelPath = os.path.join('labels','') 
            #print("\n\n\n {}".format(value))
            namelabel = create_label(key, value)
            #print(target)
            #print(target)
            try:
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
