#!/usr/bin/env python3

import glob

# get image file names
images = glob.glob('nano /supplier_data/images/*.tiff')

print(*images, sep='\n')
