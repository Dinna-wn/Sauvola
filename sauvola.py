

import numpy as np
from PIL import Image
import pylab as plt
from math import sqrt





def filtrageImage(imageIn, filtre, K ,R):
    imageOut= np.array(Image.new("1", (imageIn.shape[0], imageIn.shape[1])))

    sizeF = len(filtre)
    sizeF2 = len(filtre)//2

    for i in range(sizeF2,imageIn.shape[0]-sizeF2):
        for j in range(sizeF2,imageIn.shape[1]-sizeF2):
            moy = 0
            c = 0
            for m in range(sizeF):
                for n in range(sizeF):
                    moy += imageIn[i+m-sizeF2, j+n-sizeF2]
                    c += 1
            moy = moy / c
             ##################################################
            # del x[:]                                          # vider la liste
            # for m in range(sizeF):
            #     for n in range(sizeF):
            #         x.append(imageIn[i + m - sizeF2, j + n - sizeF2])
            # mat = np.array(x)                                 # convert to array
            # std= mat.std()                                    # std() ---> methode pour calculer l'ecart-type
            # t= moy * (1.0 + K * ((std / R ) - 1))             # calculer le seuil
            ##################################################
            std = 0.0
            effectif_de_serie = 0
            for m in range(sizeF):
                for n in range(sizeF):
                    std += (moy - imageIn[i + m - sizeF2, j + n - sizeF2]) ** 2
                    effectif_de_serie += 1
            std = sqrt(std / effectif_de_serie)
            t = moy * (1.0 + K * ((std / R) - 1))
            ##################################################
            if imageIn[i, j] > t:
                 imageOut[i, j] = 255
            else :
                 imageOut[i, j] = 0

    return imageOut




# imgpath1 = "C:\\Users\\hp\\Anaconda3\\peppers.bmp"
image = Image.open('peppers.bmp')
imageGray= image.convert('L')
imgMat = np.array(imageGray)
####################################

sizeM = int(input('get size Masque = '))
filtre = np.ones((sizeM,sizeM))/(sizeM**2)
####################################

K= 0.25
R= 128
imageF = filtrageImage(imgMat, filtre, K, R)
####################################

plt.figure(0)
plt.imshow(image)
plt.figure(1)
plt.imshow(Image.fromarray(imageF))
plt.show()





