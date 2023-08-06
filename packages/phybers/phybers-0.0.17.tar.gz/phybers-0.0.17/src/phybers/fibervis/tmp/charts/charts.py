import matplotlib.pyplot as plt
import numpy as np
'''
####################################################
# Atlas Based Segmentation
# Segmenting Time Short fiber bundle
PC1s = [
		# Bundles
		4.391,
		6.794

		# Track
]

PC2s = [
		# Bundles
		7.780,
		11.874

		# Track
]

PC3s = [
		# Bundles
		5.333,
		8.183

		# Track
]

# Segmenting Time Long fiber bundle
PC1l = [
		# Bundles
		5.552,
		8.464

		# Track
]

PC2l = [
		# Bundles
		8.760,
		13.389

		# Track
]

PC3l = [
		# Bundles
		6.463,
		9.757

		# Track
]

####################################################

####################################################
# Loading times
PC1 = [	
		# Bundles
		9.2,
		95.3,
		224.6,
		397.6,
		398.9,
		453.8,
		662.1,

		# Track
		# 10.1,
		# 1235.9,
		# 1455.6
]

PC2 = [
		# Bundles
		7.0,
		33.9,
		139.0,
		265.3,
		312.1,
		337.9,
		489.4

		# Track
]

PC3 = [
		# Bundles
		5.3,
		43.3,
		112.1,
		310.3,
		308.0,
		377.2,
		566.0

		# Track
]

####################################################
'''
####################################################
# Single ROI Segmentation
'''
# Creation
PC1 = [
		# Bundles
		43.5,
		403,
		970,
		1864,
		1877,
		# 3500,
		# 5922,

		# Track
		# 25.5,
		# 15301,
		# 182341
]

PC2 = [
		# Bundles

		422,
		1139,
		2187,
		4047,
		6848

		# Track
]

PC3 = [
		# Bundles

		354,
		944,
		1795,
		2663,
		3569,
		5643

		# Track
]

# Segmentation
PC1s = [
		# Bundles
		1.4,
		7.4,
		25.2,
		39.6,
		29.8,
		76.2,
		100,

		# Trk
		# 1.1,
		# 912.3,
		# 1196.8
]

PC2s = [
		# Bundles
		8.1,
		36.4,
		65.6,
		66.4,
		125.9,
		246.5,

		# Trk
]

PC3s = [
		# Bundles
		7.3,
		27.7,
		47.5,
		48.8,
		124.4,
		207.7

		# Trk
]

####################################################
'''
####################################################
# In place segmentation

PC1 = [
		# Bundles
		0.1,
		0.2,
		0.3,
		0.6,
		0.6,
		1.4,
		1.9,

		# Trk
		0.2,
		4.0,
		4.3,
]

PC2 = [
		0.3,
		0.4,
		0.6,
		0.7,
		1.4,
		2.0

		# Trk
]

PC3 = [
		0.5,
		0.7,
		0.5,
		0.5,
		1.0,
		1.4

		# Trk
]

####################################################

# esto es para segmentation
# PC1 = PC1s+PC1l
# PC2 = PC2s+PC2l
# PC3 = PC3s+PC3l
###################

# ROI segmentation
# PC1 = PC1s
# PC2 = PC2s
# PC3 = PC3s

data = [(i,j,k) for i,j,k in zip(PC1,PC2,PC3)]


dim = len(data[0])
w = 0.75
dimw = w / dim

legend = ['PC1', 'PC2', 'PC3']

fig, ax = plt.subplots()
x = np.arange(len(data))
for i in range(len(data[0])):
	y = [d[i] for d in data]
	b = ax.bar(x + i * dimw, y, dimw, bottom=0.001, label=legend[i])

ax.set_xticks(x + dimw)
# ax.set_xticklabels(['Short fiber Atlas\nDS6', 'Short fiber Atlas\nDS7', 'Long fiber Atlas\nDS6', 'Long fiber Atlas\nDS7','DS5', 'DS6', 'DS7'])
ax.set_xticklabels(['DS1', 'DS2', 'DS3', 'DS4','DS5', 'DS6', 'DS7'])
# ax.set_yscale('log')

ax.set_xlabel('')
ax.set_ylabel('time [ms]')
ax.legend()

plt.show()
