import os, glob
import scipy.ndimage
import numpy as np

def sorted_list(path):

    tmplist = glob.glob(path)
    tmplist.sort()

    return tmplist

def min_max_norm(x):

    min_x, max_x = x.min(), x.max()
    return (x - min_x + 1e-12) / (max_x - min_x + 1e-12)

def zoom(x, ratio):

    return scipy.ndimage.zoom(x, ratio, order=3, mode='nearest')
