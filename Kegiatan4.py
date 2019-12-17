import matplotlib.pyplot as plt
import skimage.io as io
from copy import deepcopy

img = io.imread('Logo.png')

i = deepcopy(img)

i[:,:,1]=255
i[:,:,0]=255

fig, ax = plt.subplots(ncols=2, nrows=2)

ax[0,0]. imshow(i)

ax[0,0].axis('off')
ax[0,1].axis('off')
ax[1,0].axis('off')
ax[1,1].axis('off')

plt.show()
