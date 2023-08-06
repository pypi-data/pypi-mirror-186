import matplotlib.pyplot as plt
import numpy as np

x = 			['100K',		'250K', 		'500K', 		'1M', 			'2M',		'3M']
roiSeg =		[0.0029990906,	0.008374199,	0.019432765,	0.04492927,	0.8921534,	0.5997493]
# mulRoiSeg = 	[0.0041092588,	0.011264479,	0.024749333,0.052242115,	0.62878513, 0.3080278]

fig, (ax, ax2) = plt.subplots(1,2)
y = roiSeg
y_pos = np.arange(len(y))
ax.bar(y_pos, y, align='center', alpha=0.5, color='c')

ax.set_xticks(y_pos)
ax.set_xticklabels(x)
ax.set_ylabel('Time in seconds')

########################################

# y = mulRoiSeg
# ax2.bar(y_pos, y, align='center', alpha=0.5, color='c')

# ax2.set_xticks(y_pos)
# ax2.set_xticklabels(x)

ax.grid()
ax2.grid()

plt.show()