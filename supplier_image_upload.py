#!/usr/bin/env python3

import glob
import requests

image_files = glob.glob("./supplier-data/images/*.jpeg")
url = "http://localhost/upload/"

for image in image_files:
    with open(image, "rb") as img:
        response = requests.post(url, files={"file": img})