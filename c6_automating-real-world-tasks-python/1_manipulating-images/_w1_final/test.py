#!/usr/bin/env python3

import os
from PIL import Image

for root, dirs, files in os.walk("images/"):
    for filename in files:
        if "48" in filename:
            #print(filename)
            filename = "images/" + filename
            image = Image.open(filename).convert('RGB')
            path, file = os.path.split(filename)
            file = os.path.splitext(file)[0]
            image.rotate(270).resize((128,128)).save('icons/{}.jpeg'.format(file))
