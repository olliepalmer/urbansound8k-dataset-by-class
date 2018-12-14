# collate_dataset.py
#
# a file to collate all sounds from the urban sound 8k dataset into folders by class
# must be run in python3
# or convert all input() to raw_input() to run in python2

# steps
# 1. download the urban sound 8k dataset from https://urbansounddataset.weebly.com/ 
# and save it into a folder, e.g. /username/Downloads/UrbanSound8k
# 2. run this python script using python3

import os, sys, csv
from shutil import copyfile

root = '_'
data_in = os.path.join(root,'UrbanSound8K')

while not (os.path.isdir(data_in)):
	print("can't find UrbanSound8K folder...\n\n")
	root = input('''which folder is the urbansound8k dataset saved in?
		e.g. /username/Downloads/
		(you can drag and drop a file on mac, but be sure to delete the trailing space...)\n\n''')
	data_in = os.path.join(root,'UrbanSound8K')
	print ('data_in =',os.path.isdir(data_in),data_in)

csv_file = os.path.join(data_in,'metadata/UrbanSound8K.csv')
print ('csv_file =',os.path.isfile(csv_file),csv_file)

audio_in = os.path.join(data_in,'audio')
print ('audio_in =',os.path.isdir(audio_in),audio_in)

audio_out = input('what do you want to call your new dataset?\n\n')
audio_out = os.path.join(root,audio_out)
# audio_out = os.path.join(root, 'UrbanSound8K-byclass')
if (not os.path.isdir(audio_out)):
            os.mkdir(audio_out)
print ('data_out',os.path.isdir(audio_out),audio_out)

# classes, as defined by urbansound8k
classes = ['air_conditioner', 'car_horn', 'children_playing', 'dog_bark', 'drilling', 'engine_idling', 'gun_shot', 'jackhammer', 'siren', 'street_music']
print ('classes:',classes)


def countrows():
	with open(csv_file) as f:
		reader = csv.DictReader(f)
		return sum(1 for row in reader)

numrows = countrows()

with open (csv_file) as f:
    reader = csv.DictReader(f)
    linecount = 1
    for row in reader:
        src = os.path.join(audio_in,'fold'+row['fold'],row['slice_file_name'])
        dst_fold = os.path.join(audio_out,row['classID']+'_'+row['class'])
        dst = os.path.join(dst_fold,row['slice_file_name'])
        print('copying ',linecount,'/',numrows,row['slice_file_name'],'to',dst_fold)
        if (not os.path.isdir(dst_fold)):
            os.mkdir(dst_fold)
        if (os.path.isfile(src)):
            copyfile(src,dst)
        linecount+=1