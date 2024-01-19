import os
import glob
import csv
import shutil
from PIL import Image

d = dict()
for _ in glob.glob('./dataset/images*/images/*.png', root_dir='./'):
    d[_.split('\\')[-1]] = _

res = []

with open('./dataset/Data_Entry_2017.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    for _ in data:
        if _[0] == 'Image Index':
            continue
        if _[1] == 'No Finding':
            res.append([_[0], 'Healthy'])
        if _[1] == 'Cardiomegaly':
            res.append([_[0], 'Cardiomegaly'])

with open('./dataset/train_val_list.txt', 'r') as f:
    train_val_list = f.read().splitlines()

with open('./dataset/test_list.txt', 'r') as f:
    test_list = f.read().splitlines()

train_res = []
test_res = []

for _ in res:
    if _[0] in train_val_list:
        train_res.append(_)
    elif _[0] in test_list:
        test_res.append(_)

if not os.path.exists('./dataset/train'):
    os.mkdir('./dataset/train')

if not os.path.exists('./dataset/test'):
    os.mkdir('./dataset/test')

if not os.path.exists('./dataset/train/Healthy'):
    os.mkdir('./dataset/train/Healthy')

if not os.path.exists('./dataset/test/Healthy'):
    os.mkdir('./dataset/test/Healthy')

if not os.path.exists('./dataset/train/Cardiomegaly'):
    os.mkdir('./dataset/train/Cardiomegaly')

if not os.path.exists('./dataset/test/Cardiomegaly'):
    os.mkdir('./dataset/test/Cardiomegaly')

for _ in train_res:
    img = Image.open(d[_[0]])
    img = img.convert('RGB')
    if _[1] == 'Healthy':
        img.save('./dataset/train/Healthy/' + _[0].replace('.png', '.jpg'))
    elif _[1] == 'Cardiomegaly':
        img.save('./dataset/train/Cardiomegaly/' + _[0].replace('.png', '.jpg'))

for _ in test_res:
    img = Image.open(d[_[0]])
    img = img.convert('RGB')
    if _[1] == 'Healthy':
        img.save('./dataset/test/Healthy/' + _[0].replace('.png', '.jpg'))
    elif _[1] == 'Cardiomegaly':
        img.save('./dataset/test/Cardiomegaly/' + _[0].replace('.png', '.jpg'))

# print(f'Wrote {len(res)} lines to labels.txt, total {sum([int(_[1] == "Cardiomegaly") for _ in res])} positive samples.')