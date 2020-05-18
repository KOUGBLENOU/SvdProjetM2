######################################################
#       PROJET M2 APPRENTISSAGE NON SUPERVISEE       #
#       APPLICATION.py FILE                          #
#       AUTHORS :                                    #
#           *** Masood S.                            #
#           *** Ben A.                               #
#           *** Frank K2                             #
#       LAST UPDATE : 06/02/2020                     #
#       OBJECT :                                     #
#               Test of Remake function on a         #
#               picture "image.png"                  #
######################################################

# ============================================== Frank Add
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as mp
import matplotlib.image as img
import matplotlib.pyplot as plt
import math as mt
import remake


image=img.imread("image.png")

if (image.dtype == np.float32):
    image = (image * 255).astype(np.uint8)
    
n_elements = 5

Blue = remake.remake(image[:, :,2], n_elements)
Green = remake.remake(image[:, :,1], n_elements)
Red = remake.remake(image[:, :,0], n_elements)
Rimage = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

Rimage[:, :,1] = Green
Rimage[:, :,0] = Red
Rimage[:, :,2] = Blue
plt.imshow(Rimage)
plt.show()

