import albumentations as A
import glob
import os
import random
from PIL import Image
import numpy as np

GEN_IMAGE_COUNT = 1000

def transform_image(img):
    transform = A.Compose([
        A.RandomBrightnessContrast(p=0.2),
        A.RandomGamma(p=0.2),
        A.GaussNoise(p=0.2)
    ])
    return transform(image=img)['image']

def gen_image(input_path, save_path='./sample_dataset/gen_dataset/'):
    lis = []
    for _ in glob.glob(input_path + '*.jpg'):
        img = Image.open(_)
        lis.append(np.asarray(img))

    for _ in range(GEN_IMAGE_COUNT):
        img = random.choice(lis)
        img = transform_image(img)
        img = Image.fromarray(img)
        img.save(save_path + str(_) + '.jpg')


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

if not os.path.exists('sample_dataset/gen_dataset/'):
    os.mkdir('sample_dataset/gen_dataset/')

for _ in labels:
    if not os.path.exists('./sample_dataset/gen_dataset/' + _):
        os.mkdir('./sample_dataset/gen_dataset/' + _)

for _ in labels:
    print(f"Generating images for { _ }")
    gen_image('./sample_dataset/dataset/' + _ + '/', './sample_dataset/gen_dataset/' + _ + '/')
