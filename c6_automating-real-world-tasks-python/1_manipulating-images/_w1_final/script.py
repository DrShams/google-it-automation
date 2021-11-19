#!/usr/bin/env python3

from PIL import Image
from glob import glob
import os

for file in glob('images/ic_*'):
    image = Image.open(file).convert('RGB')
    # print(image.format, image.size, image.mode) # test
    path, filename = os.path.split(file)
    filename = os.path.splitext(filename)[0] # get filename without extension
    image.rotate(270).resize((128,128)).save('icons/{}.jpeg'.format(filename))

print('OK')
