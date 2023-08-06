import matplotlib.pyplot as plt
import numpy as np

x = 			['100K',		'250K', 		'500K', 		'1M', 			'2M',			'3M']
metadata_seg =	[0.00022338724,	0.0003873657,	0.0006900537,	0.0011906843,	0.0023003223,	0.0035183781]

fig, ax = plt.subplots(1)
y = np.array(metadata_seg)*1000
y_pos = np.arange(len(y))
ax.bar(y_pos, y, align='center', alpha=0.5, color='c')

ax.set_xticks(y_pos)
ax.set_xticklabels(x)
ax.set_ylabel('Time [ms]')

########################################

# y = mulRoiSeg
# ax2.bar(y_pos, y, align='center', alpha=0.5, color='c')

# ax2.set_xticks(y_pos)
# ax2.set_xticklabels(x)

ax.grid()
# ax2.grid()

plt.show()