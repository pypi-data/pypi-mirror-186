import numpy as np
import Framework.CExtend.cfuncs as cfuncs
import os

in_file = 'D:/Codes/UDEC/Database/Atlas Segmentation/sujetos segmentar/955k.bundles'
out_file = 'D:/Desktop/'+str(nFinalFiber)+'.bundle'

# Data read
###########
bunFile = in_file + 'data'
dataSize = os.path.getsize(bunFile)

ns = dict()
with open(in_file) as f:
	exec(f.read(), ns)

bundlescount = ns[ 'attributes' ][ 'bundles' ]
curvescount = ns[ 'attributes' ][ 'curves_count' ]

bundlesName = bundlescount[::2]
bundlesStart = bundlescount[1::2]

points = np.empty(dataSize//4-curvescount, dtype=np.float32)
normals = np.empty(dataSize//4-curvescount, dtype=np.float32)
color = np.empty((dataSize//4-curvescount)//3, dtype=np.int32)
elements = np.empty((dataSize//4-curvescount)//3+curvescount, dtype=np.uint32)
fiberSizes = np.empty(curvescount, dtype=np.int32)

bundlesInterval = np.array(bundlesStart+[curvescount], dtype=np.int32)

cfuncs.readBundleFile(
	bunFile.encode('utf-8'),
	points.ctypes.data,
	normals.ctypes.data,
	color.ctypes.data,
	elements.ctypes.data,
	fiberSizes.ctypes.data,
	bundlesInterval.ctypes.data,
	curvescount,
	bundlesInterval.size)

print('read with fiber: ', curvescount)

# Data segment
##############
nFinalFiber = 500000
selectedFiber = np.zeros(curvescount, dtype=np.int8)

step = curvescount/nFinalFiber

i = 0
while i*step<curvescount:
# for i in range(0, curvescount, step):
	selectedFiber[int(i*step)] = 1
	i += 1

print('selectedFiber: ', selectedFiber.sum())

# Export file
#############
bundleCount = np.zeros(len(bundlesName), dtype=np.int32)
bundlesStart2 = np.append(bundlesStart, curvescount).astype(np.int32)

cfuncs.ROISegmentationExportbundlesdata(
	(out_file+'data').encode('utf-8'),
	len(bundlesName),
	bundlesStart2.ctypes.data,
	fiberSizes.ctypes.data,
	bundleCount.ctypes.data,
	points.ctypes.data,
	selectedFiber.ctypes.data)

ncount = (selectedFiber[:curvescount] != 0).sum()

# wrtie minf file
minf = """attributes = {\n    'binary' : 1,\n    'bundles' : %s,\n    'byte_order' : 'DCBA',\n    'curves_count' : %s,\n    'data_file_name' : '*.bundlesdata',\n    'format' : 'bundles_1.0',\n    'space_dimension' : 3\n  }\n"""

bundlesstr = []
offset = 0

for name, bundleSize in zip([bundlesName[i] for i in range(len(bundlesName)) if bundleCount[i] != 0], bundleCount[bundleCount != 0]):
	bundlesstr.append(name)
	bundlesstr.append(offset)
	offset += bundleSize
		
bundlesstr = str(bundlesstr)
bundlesstr = bundlesstr[0] + ' ' + bundlesstr[1:-1] + ' ' + bundlesstr[-1]

with open(out_file, 'w') as file:
	file.write( minf % ( bundlesstr, ncount ) )