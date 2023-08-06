import matplotlib.pyplot as plt
import numpy as np

x = 			[100000,			250000,				500000,				1000000,			2000000,			3000000]
linesFps =		[624.543601073118,	248.0459831664723,	122.4469068449910,	64.211888466434,	14.812665827245988,	15.60350295386914]
cylinderFps = 	[111.777186370606,	45.16586816589467,	22.50339841103735,	11.900713983992,	2.6388041559725983, 2.4225650138147383]

fig, (ax, ax2) = plt.subplots(1,2)
y = linesFps
b = ax.plot(x, y, color='c')

ax.set_xticks([250000,500000,1000000,2000000,3000000])
ax.set_xticklabels(['250K', '500K', '1M', '2M','3M'])

# ax.set_xlabel('Datasets')
ax.set_ylabel('Frames per second')


y = cylinderFps
b = ax2.plot(x, y, color='#eeaf3f')

# ax2.set_xticks(x)
# ax2.set_xticklabels(['DS1', 'DS2', 'DS3', 'DS4','DS5', 'DS6', 'DS7', 'DS8', 'DS9'])

# ax2.set_xlabel('Datasets')

# ax.set(title='Average frame rate for tratcs\nrendering as lines')
# ax2.set(title='Average frame rate for tratcs\nrendering as cylinders')

ax.grid()
ax2.grid()

plt.show()