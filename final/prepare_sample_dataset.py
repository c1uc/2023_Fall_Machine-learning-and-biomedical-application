import os
import glob
import csv
import shutil
from PIL import Image

d = dict()
for _ in glob.glob('./sample/images/*.png', root_dir='./'):
    d[_.split('\\')[-1]] = _

res = []

with open('./sample/sample_labels.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    for _ in data:
        if _[0] == 'Image Index':
            continue
        if _[1] == 'No Finding':
            res.append([_[0], 'Healthy'])
        if _[1] == 'Cardiomegaly':
            res.append([_[0], 'Cardiomegaly'])


if not os.path.exists('./sample/dataset'):
    os.mkdir('./sample/dataset')

if not os.path.exists('./sample/dataset/Healthy'):
    os.mkdir('./sample/dataset/Healthy')

if not os.path.exists('./sample/dataset/Cardiomegaly'):
    os.mkdir('./sample/dataset/Cardiomegaly')

for _ in res:
    img = Image.open(d[_[0]])
    img = img.convert('RGB')
    if _[1] == 'Healthy':
        img.save('./sample/dataset/Healthy/' + _[0].replace('.png', '.jpg'))
    elif _[1] == 'Cardiomegaly':
        img.save('./sample/dataset/Cardiomegaly/' + _[0].replace('.png', '.jpg'))

# print(f'Wrote {len(res)} lines to labels.txt, total {sum([int(_[1] == "Cardiomegaly") for _ in res])} positive samples.')