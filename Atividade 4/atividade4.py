import numpy as np
import matplotlib.pyplot as plt
import cv2
import math
import imageio as im
from PIL import Image

#root_path = "C:\Users\Gabriel P H\Documents\Gabriel\UFU\Multimidia\MultimidiaRepo\Atividade 4"

skull = cv2.imread("./skull.tif",0)
skull = Image.fromarray(skull)
skull = np.array(skull)
plt.imshow(skull, cmap='gray')
plt.show()

def histogram_array(image):
    array = np.zeros((256,), dtype=int)
    for j in range(len(array)):
        for i in range(len(array)):
            array[image[i][j]] += 1

    return array
    
def ponto_limiarizacao(array_image):       
    arr1 = array_image[0:128]
    arr2 = array_image[129:255]
        
    m1 = np.max(arr1)
    m2 = np.max(arr2)
    
    for i in range(len(array_image)):
        if array_image[i] == m1:
            if i < 129:
                x1 = i
            print("x1", x1)
        if array_image[i] == m2:
            if i >= 129:
                x2 = i
            print("x2", x2)
            
    arr3 = array_image[x1:x2]
    print("arr3", arr3)
        
    m3 = np.min(arr3)
    print("m3", m3)
    
    for i in range(len(array_image)):
        if array_image[i] == m3:
            if i >= x1 and i <= x2:
                x3 = i
                break
    
    print("x3", x3)
    return x3
    

def limiarizacao(ponto, image):
    num_rows, num_cols = image.shape
    
    for j in range(num_cols):
        for i in range(num_rows):
            if image[i][j] < ponto:
                image[i][j] = 0
            else:
                image[i][j] = 255
                
    return image
    
    
histr = histogram_array(skull)
print(histr)

plt.plot(histr)
plt.show()

ponto = ponto_limiarizacao(histr)
print("Ponto", ponto)

skull = limiarizacao(ponto, skull)
plt.imshow(skull, cmap='gray')
plt.show()

boat = cv2.imread("./boat.tiff",0)
boat = Image.fromarray(boat)
boat = np.array(boat)
plt.imshow(boat, cmap='gray')
plt.show()
print(boat)

histr = histogram_array(boat)
print(histr)
plt.plot(histr)
plt.show()
ponto = ponto_limiarizacao(histr)
print("Ponto boat", ponto)
boat = limiarizacao(ponto, boat)
plt.imshow(boat, cmap='gray')
plt.show()

lena = cv2.imread("./lena.tiff",0)
lena = Image.fromarray(lena)
lena = np.array(lena)
plt.imshow(lena, cmap='gray')
plt.show()

histr = histogram_array(lena)
ponto = ponto_limiarizacao(histr)
lena = limiarizacao(ponto, lena)
plt.imshow(lena, cmap='gray')
plt.show()



