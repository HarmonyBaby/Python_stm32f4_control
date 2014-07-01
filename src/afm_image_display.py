#!/usr/share/bin python
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.axes_grid1 import ImageGrid
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def plot(data):
    fig=plt.figure()
    grid = ImageGrid(fig, 111, # similar to subplot(111)
                nrows_ncols = (1, 1), # creates 2x2 grid of axes
                axes_pad=0.1, # pad between axes in inch.
                )
    grid[0].imshow(data)
    plt.show(fig)
    
def plot_2d(data):
    colormap=matplotlib.cm.pink
    plt.imshow(data,cmap=colormap)
    plt.show()

def plot_3d(data):
    x=range(0,256)
    y=range(0,256)
    X,Y=np.meshgrid(x,y)
    colormap=matplotlib.cm.jet
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X,Y,data)
    
    
    
    plt.show(fig)



