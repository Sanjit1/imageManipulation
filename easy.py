from matplotlib import pyplot as plotter
import os
import PIL as a_very_soft_pillow
from PIL import Image

cwd = os.path.dirname(os.path.abspath(__file__))
nyan_jpg = os.path.join(cwd, 'nyan.jpg')
nyan_image = a_very_soft_pillow.Image.open(nyan_jpg)
fig, axes = plotter.subplots(1, 1)
axes.imshow(nyan_image, interpolation='none')


plotter.show()

