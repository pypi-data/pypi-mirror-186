import sys, os
import numpy as np
from scipy import sparse
import read_write_bundle as BT
import nibabel as nib

############################



if 1:
	print x

	acpc_dc2standard = '/home/fibras2/HCP1200/100206/preproc/100206/T1w/Diffusion/transformaciones/xfms/acpc_dc2standard.nii.gz'#'/home/fibras2/HCP1200/100307/preproc/100307_Structural/MNINonLinear/xfms/acpc_dc2standard.nii.gz'#


	imfile = acpc_dc2standard
	fibras = '/home/fibras2/HCP1200/100206/IN/5Msift_t.bundles'#'/home/fibras2/HCP1200/100307/IN/whole_brain100k.bundles'#

	vol = nib.load(imfile)
	arr = vol.get_data()

	points=BT.read_bundle(fibras)

	a=np.array([np.float32(0),np.float32(0),np.float32(0)])
	points2=[]
	for i in range(len(points)):
		l=[]
		for j in range(len(points[i])):#l=[a]*len(points[i])
			l.append(a)	
		l=np.array(l)
		points2.append(l)
	a=np.array([np.float32(0),np.float32(0),np.float32(0)])

	print 'o'	
	for i in range(len(points)):
		for j in range(len(points[i])):
			for k in [0,1,2]:#asumiendo orden x y z
				traslacion=arr[int(points[i][j][0]/2)][108-int(points[i][j][1]/2)][90-int(points[i][j][2]/2)][k]
				if k==0:
					points2[i][j][k]=points[i][j][k]-(traslacion*1)
				else:
					points2[i][j][k]=points[i][j][k]+(traslacion*1)

	print 'k'

	BT.write_bundle('/home/fibras2/HCP1200/100206/IN/5Msift_t_MNI.bundles', points2)
	#BT.write_bundle('/home/fibras2/HCP1200/100206/IN/whole_brain100k_yzinv_p1-x.bundles', points2)





