#!/usr/bin/env python
# coding: utf-8
from transformers import AutoImageProcessor
from transformers import pipeline
import matplotlib.pyplot as plt
from PIL import Image
import os

model_name = './image_aug_model_epoch_10_01-07-24-16-05-41'
processor = AutoImageProcessor.from_pretrained(model_name)

classifier = pipeline("image-classification", model=model_name, tokenizer=processor)

imgs = os.listdir('./sample_images')

fig, ax = plt.subplots(4, 4, figsize=(10, 10))

for i in range(15):
    path = f"./sample_images/{imgs[i]}"
    img = Image.open(path)
    res = classifier(img)
    label = imgs[i]
    for _ in range(3):
        label += f"\n{res[_]['label']} ({res[_]['score']:.2f})"
    ax[i // 4, i % 4].imshow(img)
    ax[i // 4, i % 4].set_title(label)
    ax[i // 4, i % 4].axis("off")

ax[3, 3].axis("off")
plt.tight_layout()

plt.savefig("sample_images.png")
