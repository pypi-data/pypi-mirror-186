#primero usar tcktobundles, luego esto

import nibabel as nb
from claulib import *
import read_write_bundle as BT
import nibabel.streamlines.tck as TF

tf2=rtxt('/media/fibras2/Disco4T/HCP1200/sf3.txt')

malos=[]
for s in tf2:
	try:
		fibra=TF.TckFile('/media/fibras2/Disco4T/HCP1200/ClusterServer/Fibras3Listos/'+s+'/3Msift.tck')
		fibTCK=fibra.load('/media/fibras2/Disco4T/HCP1200/ClusterServer/Fibras3Listos/'+s+'/3Msift.tck').streamlines

		fibs=[]
		for i in range(len(fibTCK)):
		    fib=fibTCK[i]#agregadas
		    fib.setflags(write=True)#
		    #for j in range(len(fib)):#
		    #    fib[j][2]=90-fib[j][2]#2
		    #    fib[j][0]=90-fib[j][0]#
		    #    fib[j][1]=90-fib[j][1]#
	
		    fibs.append(fib)#(fibTCK[i])#[0]
		BT.write_bundle('/media/fibras2/Disco4T/HCP1200/ClusterServer/Fibras3Listos/'+s+'/3Msift.bundles',fibs)
		print s,'ok'
	except:
		print s,'noooooo'
		malos.append(s)






#----------------------------
T=np.load('/home/fibras2/test/tck2bundles.npy')



def apply_aff_point(inPoint,T):
  Tfrm = T#N.array([[0.6, 0, 0, 0],[0, -0.6, 0, 5],[ 0, 0, -0.6, 0],[0, 0, 0, 1]])
  tmp = Tfrm * N.transpose(N.matrix(N.append(inPoint,1)))
  outpoint = N.squeeze(N.asarray(tmp))[0:3]
  return outpoint
  
def apply_aff_bundle(bunIn,bunOut):
  points=BT.read_bundle(bunIn)
  newPoints=[]
  for fib in points:
    newfib=[]
    for p in fib:
      pt=apply_aff_point(p,T)
      newfib.append((pt))
    newPoints.append(N.asarray(newfib,dtype=N.float32))
  BT.write_bundle(bunOut, newPoints)


apply_aff_bundle('/home/fibras2/HCP1200/100206/IN/5Msift.bundles','/home/fibras2/HCP1200/100206/IN/5Msift_t.bundles')
