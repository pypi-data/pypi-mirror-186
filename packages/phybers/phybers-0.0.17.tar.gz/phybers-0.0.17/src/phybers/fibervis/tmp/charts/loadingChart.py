import matplotlib.pyplot as plt
import numpy as np

f100k =	[0.4935,  0.4654,  0.4834,  0.4788,  0.5023,  0.3239,  0.6005,  0.3118,  0.3278,  0.3279]
f250k =	[0.7991,  0.7978,  0.8980,  0.8109,  0.8039,  0.7659,  1.0620,  0.7912,  0.7665,  0.9104]
f500k =	[1.7766,  1.7514,  1.5221,  1.4362,  1.5537,  1.4820,  1.4937,  1.4958,  1.4919,  1.5698]
f1M =	[4.6036,  4.3636,  4.4898,  4.3922,  4.4424,  4.3410,  4.4459,  4.4363,  4.3115,  4.4789]
f2M =	[23.6473, 22.3643, 21.3663, 21.5409, 21.6628, 21.4533, 24.8864, 23.8970, 21.6687, 23.4047]
f3M =	[43.8405, 41.2187, 24.7727, 25.3930, 25.4690, 25.1024, 25.1797, 25.1902, 24.8443, 25.7849]

x = 			[100000,			250000,				500000,				1000000,		2000000,			3000000]
loadingTimes =	[np.mean(f100k),	np.mean(f250k),		np.mean(f500k),		np.mean(f1M),	np.mean(f2M),		np.mean(f3M)]

print(loadingTimes)

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