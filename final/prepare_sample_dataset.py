import os
import glob
import csv
import shutil
from PIL import Image

d = dict()
for _ in glob.glob('sample_dataset/images/*.png', root_dir='./'):
    d[_.split('\\')[-1]] = dict()
    d[_.split('\\')[-1]]['path'] = _

res = []

with open('sample_dataset/sample_labels.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)
    for _ in data:
        if _[0] == 'Image Index':
            continue
        if _[1] == 'No Finding':
            d[_[0]]['label'] = ['Healthy']
        else:
            d[_[0]]['label'] = _[1].split('|')


if not os.path.exists('sample_dataset/dataset'):
    os.mkdir('sample_dataset/dataset')

labels = [
    'Healthy',
    'Atelectasis',
    'Consolidation',
    'Infiltration',
    'Pneumothorax',
    'Edema',
    'Emphysema',
    'Fibrosis',
    'Effusion',
    'Pneumonia',
    'Pleural_Thickening',
    'Cardiomegaly',
    'Nodule',
    'Mass',
    'Hernia'
]

for _ in labels:
    if not os.path.exists('./sample_dataset/dataset/' + _):
        os.mkdir('./sample_dataset/dataset/' + _)

for _ in d.keys():
    img = Image.open(d[_]['path'])
    img = img.convert('RGB')
    for __ in d[_]['label']:
        img.save('./sample_dataset/dataset/' + __ + '/' + _.replace('.png', '.jpg'))
