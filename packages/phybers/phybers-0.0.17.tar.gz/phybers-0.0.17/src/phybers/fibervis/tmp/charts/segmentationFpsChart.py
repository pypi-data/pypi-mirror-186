import matplotlib.pyplot as plt
import numpy as np

x = 					[100000,			250000,				500000,				1000000,						3000000]
withTransparent =		[395.8767756637254, 162.79950014297657,	83.20721314971476,	43.6462319042056,				6.814494658233244]
withoutTransparent = 	[1143.426752542796,	492.14163520144615,	256.94503464147965,	137.7600026070357,				20.47948595040301]

fig, (ax, ax2) = plt.subplots(1,2)
y = withTransparent
b = ax.plot(x, y, color='c')

ax.set_xticks([250000,500000,1000000,2000000,3000000])
ax.set_xticklabels(['250K', '500K', '1M', '2M','3M'])

# ax.set_xlabel('Datasets')
ax.set_ylabel('Frames per second')


y = withoutTransparent
b = ax2.plot(x, y, color='c')

# ax2.set_xticks(x)
# ax2.set_xticklabels(['DS1', 'DS2', 'DS3', 'DS4','DS5', 'DS6', 'DS7', 'DS8', 'DS9'])

# ax2.set_xlabel('Datasets')

# ax.set(title='Average frame rate for tratcs\nrendering as lines')
# ax2.set(title='Average frame rate for tratcs\nrendering as cylinders')

ax.grid()
ax2.grid()

plt.show()
