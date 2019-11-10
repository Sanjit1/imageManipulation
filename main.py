import matplotlib.pyplot as plotter
import os.path
from PIL import Image

cwd = os.path.dirname(os.path.abspath(__file__))
nyan_jpg = os.path.join(cwd, 'nyan.jpg')
nyan_cat = Image.open(nyan_jpg)
fig, axes = plotter.subplots(1, 1)
axes.imshow(nyan_cat, interpolation='none')
fig.show()
