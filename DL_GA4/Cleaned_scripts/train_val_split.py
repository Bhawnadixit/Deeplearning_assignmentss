import os
import numpy as np
import shutil
import random
import pandas as pd
import collections
from distutils.dir_util import copy_tree

path1 = "C:\\Users\\32470\\Downloads\\Musicnet\\Spectograms_fft\\"
path2 = path1+'train_classes\\'

# to split train and val from the structure should be like this:
# -train_set
# ---cls1
# -----folders with images
# -------images with folder names 1727_1.png
# ---cls2
# -----folders with images

# path2 = path1+"train_classes\\"
#
# o_path = path1+"train_classes\\"           # path to do the splitting
meta_data = pd.read_csv('C:\\Users\\32470\\Downloads\\Musicnet\\musicnet\\musicnet_metadata.csv')

idx = []
for i in meta_data["composer"]:
    idx.append(i)

cd = []
classes_dir = []
# CREATES FOLDER BASED ON CLASSES
for x, y in collections.Counter(idx).items():
    if y > 1:
        cd.append(x)
        # print(y)
        classes_dir.append(path2+x) # print(x)

print(classes_dir)

# # # Creating Train / Val / Test folders (One time use)
if not os.path.exists(path1+"splitted"):
    os.mkdir(path1+"splitted")

root_dir = path1+'splitted\\'
# classes_dir = ['/class1', 'class2', 'class3', 'class4']

val_ratio = 0.10
# test_ratio = 0.05

def train_val_split(root_dir, classes_dir):
    for cls, clas in zip(cd, classes_dir):
        os.makedirs(root_dir +'train\\' + cls)
        os.makedirs(root_dir +'val\\' + cls)
        # os.makedirs(root_dir +'/test' + cls)

        # Creating partitions of the data after shuffeling
        src = path2+cls # Folder to copy images from
        # print(src)
        allFileNames = os.listdir(src)
        # print(allFileNames)
        # np.random.shuffle(allFileNames)
        train_FileNames, val_FileNames = np.split(np.array(allFileNames),
                                                                  [int(len(allFileNames)* (1 - val_ratio))])

        #
        trainFileNames = [src+'\\'+ name for name in train_FileNames.tolist()]
        # print(trainFileNames)
        valFileNames = [src+'\\' + name for name in val_FileNames.tolist()]
        # print(val_FileNames)
        # test_FileNames = [src+'/' + name for name in test_FileNames.tolist()]
        #
        print('Total images: ', len(allFileNames))
        print('Training: ', len(trainFileNames))
        print('Validation: ', len(valFileNames))
        # print('Testing: ', len(test_FileNames))

        # # Copy-pasting images
        # print('TRAIN FILE NAMES')
        for name in trainFileNames:
            print('TRAIN FILE', name.split('\\')[-1])
            # print(name)
            a = os.path.join(root_dir +'train' +'\\'+ cls+'\\')
            copy_tree(name, a)

        # print('VAL FILE NAMES')
        for name in valFileNames:
            print('VALIDATION FILE', name.split('\\')[-1])
            b = os.path.join(root_dir +'val'+'\\' + cls+'\\')
        #     print(name)
            copy_tree(name, b)


train_val_split(root_dir, classes_dir)
        # for name in test_FileNames:
        #     shutil.copy(name, root_dir +'/test' + cls)

# OUTPUT FOR EACH CLASS SPLITTING INTO TRAIN AND VALIDATION
# Total images:  29
# Training:  26
# Validation:  3
# Total images:  22
# Training:  19
# Validation:  3
# Total images:  8
# Training:  7
# Validation:  1
# Total images:  9
# Training:  8
# Validation:  1
# Total images:  2
# Training:  1
# Validation:  1
# Total images:  24
# Training:  21
# Validation:  3
# Total images:  4
# Training:  3
# Validation:  1
# Total images:  4
# Training:  3
# Validation:  1
# Total images:  64
# Training:  57
# Validation:  7
# Total images:  154
# Training:  138
# Validation:  16