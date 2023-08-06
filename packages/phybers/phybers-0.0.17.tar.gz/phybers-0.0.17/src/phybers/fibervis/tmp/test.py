# import nibabel as nib
import numpy as np

mat = np.load("../trkMat.npy")
axes_2_flip = 2

print(mat)
mat[axes_2_flip, axes_2_flip] *= -1
mat[axes_2_flip,3] += 180
print(mat)

np.save("../trkMat2", mat)