

import numpy as np
from PIL import Image
import pylab as plt

#chargement en mode NDG et conversion en matrice NUMPY
imNDG = Image.open('peppers.bmp').convert('L')

imgMat = np.array(imNDG) #convertion d l'image vers une matrice

sizeM = int(input('get size Masque '))
filtre = np.ones((sizeM,sizeM))/(sizeM**2)
#filtre = np.array([[1, 1, 1],[1, -8, 1],[1, 1, 1]])



def filtrageImage(imageIn, filtre):
    imageOut= np.array(Image.new("L", (imageIn.shape[0], imageIn.shape[1])))

    sizeH, sizeW = imageIn.shape
    sizeF = len(filtre)
    sizeF2 = len(filtre)//2

    for i in range(sizeF2,imageIn.shape[0]-sizeF2):
        for j in range(sizeF2,imageIn.shape[1]-sizeF2):
            somme = 0
            for m in range(sizeF):
                for n in range(sizeF):
                    somme += imageIn[i+m-sizeF2,j+n-sizeF2]*filtre[m,n]
            imageOut[i,j] = somme
    return imageOut


imageF = filtrageImage(imgMat, filtre)

plt.figure(0)
plt.imshow(imNDG)

plt.figure(1)
plt.imshow(Image.fromarray(imageF))

plt.show()

