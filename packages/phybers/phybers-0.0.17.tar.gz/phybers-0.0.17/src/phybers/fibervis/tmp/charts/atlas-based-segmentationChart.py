import matplotlib.pyplot as plt
import numpy as np

f100k =	[0.9376, 0.9056, 0.9027, 0.9009, 0.9164, 0.9099, 0.8632, 0.8691, 0.8668, 0.8588]
f250k =	[2.3657, 2.1752, 2.1433, 2.1602, 2.1682, 2.1363, 2.1403, 2.1263, 2.1313, 2.1443]
f500k =	[4.2883, 4.3174, 4.3000, 4.2985, 4.6694, 4.3046, 4.2885, 4.3962, 4.3035, 4.2825]
f1M =	[8.1229, 8.1223, 8.2170, 8.1153, 8.1402, 8.1353, 8.1432, 8.1602, 8.1313, 8.1133]
# f2M
f3M =	[24.8557, 24.7398, 24.7588, 24.8003, 24.9273, 24.8373, 24.8619, 24.7632, 24.7857, 24.8016]

x = 			[100000,			250000,				500000,				1000000,						3000000]
longFiber_atlas =	[np.mean(f100k),		np.mean(f250k),		np.mean(f500k),		np.mean(f1M),					np.mean(f3M)]

print('Long fiber atlas segmentation: ',longFiber_atlas)

f100k =	[0.6852, 0.6836, 0.6742, 0.6763, 0.6852, 0.6921, 0.6842, 0.6769, 0.6782, 0.6852]
f250k =	[1.6755, 1.6865, 1.6486, 1.6765, 1.6596, 1.6576, 1.6506, 1.6625, 1.6835, 1.6855]
f500k =	[3.3241, 3.2972, 3.2992, 3.3012, 3.3281, 3.3195, 3.2982, 3.3211, 3.3311, 3.3530]
f1M =	[6.3510, 6.3420, 6.3281, 6.3449, 6.3600, 6.3351, 6.3709, 6.3749, 6.3440, 6.3151]
# f2M
f3M =	[21.2672, 21.5070, 21.2211, 21.2542, 21.1797, 21.3959, 21.2768, 21.2174, 21.2950, 21.2951]

shortFiber_atlas =	[np.mean(f100k),		np.mean(f250k),		np.mean(f500k),		np.mean(f1M),					np.mean(f3M)]

print('Short fiber atlas segmentation: ',shortFiber_atlas)

# fig, (ax, ax2) = plt.subplots(1,2)
# y = linesFps
# b = ax.plot(x, y, color='c')

# ax.set_xticks([250000,500000,1000000,2000000,3000000])
# ax.set_xticklabels(['250K', '500K', '1M', '2M','3M'])

# # ax.set_xlabel('Datasets')
# ax.set_ylabel('Frames per second')


# y = cylinderFps
# b = ax2.plot(x, y, color='#eeaf3f')

# # ax2.set_xticks(x)
# # ax2.set_xticklabels(['DS1', 'DS2', 'DS3', 'DS4','DS5', 'DS6', 'DS7', 'DS8', 'DS9'])

# # ax2.set_xlabel('Datasets')

# # ax.set(title='Average frame rate for tratcs\nrendering as lines')
# # ax2.set(title='Average frame rate for tratcs\nrendering as cylinders')

# ax.grid()
# ax2.grid()

# plt.show()


