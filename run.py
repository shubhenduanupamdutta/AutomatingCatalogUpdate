#!/usr/bin/env python3

import os
import requests
import glob

description_files = glob.glob("./supplier-data/descriptions/*.txt")
URL_ENDPOINT = "34.139.85.112/fruits/"
image_files = glob.glob("./supplier-data/images/*.jpeg")

fruits = []
for description_file in description_files:
    # parse the description file
    with open(description_file) as file:
        lines = file.readlines()
        fruit = {
            "name": lines[0].strip(),
            "weight": int(lines[1].strip().split()[0]),
            "description": lines[2].strip(),
            "image_name": description_file.split("/")[-1].replace(".txt", ".jpeg")
        }
        fruits.append(fruit)

# post the fruit data to the website
for fruit in fruits:
    response = requests.post(URL_ENDPOINT, json=fruit)
    response.raise_for_status()