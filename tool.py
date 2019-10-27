def int_to_bin_string(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i //= 2
    if len(s) != 8:
        l = abs(len(s) - 8)
        for i in range(l):
            s ="0"+s
    return s

import imageio
import numpy as np

def bin_to_int(i):
    i = str(i)
    arr = [128, 64, 32, 16, 8, 4, 2, 1]
    sm = 0
    for index in range(len(i)):
        if i[index] == "1":
            sm+= arr[index]
    return sm
        

def imageToBinary(filename):
    im = imageio.imread(filename)
    print("Data type : "+str(im.dtype))
    x = im.shape[0]
    y = im.shape[1]
    z = im.shape[2]
    imageBin = [[[0 for z in range(z)] for j in range(y)] for i in range(x)]
    for zz in range(z):
        for yy in range(y):
            for xx in range(x):
                imageBin[xx][yy][zz]= int_to_bin_string(int(im[xx][yy][zz]))
    return imageBin

def binaryToImage(imageBin, filename):
    x = len(imageBin)
    y = len(imageBin[0])
    z = len(imageBin[0][0])
    newBin = [[[0 for z in range(z)] for j in range(y)] for i in range(x)]
    for zz in range(z):
        for xx in range(x):
            for yy in range(y):
                newBin[xx][yy][zz]= bin_to_int(imageBin[xx][yy][zz])
    newBin = np.array(newBin, dtype=np.uint8)
    print(newBin.dtype)
    imageio.imwrite(filename, newBin[:, :, :])



def test(filename):
    im = imageio.imread(filename)
    for pixel in iter(im.getdata()):
        print(pixel)