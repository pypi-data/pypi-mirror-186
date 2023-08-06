import os
import sys
import shlex
import subprocess as sp

#indir="data/100206/100206_MNI.bundles"
#in_npoints="21" #puede variar, elección del usuario, se recomienda usar a 21 puntos.
#outdir="data/100206/100206_MNI_21p.bundles"
#sp.run(['./sampled_npoints/sliceFibers', indir, outdir, in_npoints])

def sampling(indir, in_npoints, outdir):
    pathname = os.path.dirname(__file__)

    if os.path.exists(os.path.join(pathname, 'sampled_npoints','sliceFibers')):
        print("dbindex exists.")
    else:
        print("dbindex does not exist in path. Compiling it: ")
        sp.run(['gcc', os.path.join(pathname, 'sampled_npoints','sliceFibers.c'), '-o', os.path.join(pathname, 'sampled_npoints','sliceFibers'), '-lm', '-w'])
        
        if os.path.exists(os.path.join(pathname, 'sampled_npoints','sliceFibers')):
            print("Target directory has been created successfully.")

        else: 
            print("Target directory still doesn't exist. Exiting...")
            exit()
    
    sp.run([ os.path.join(pathname, 'sampled_npoints','sliceFibers'), indir, outdir, in_npoints])
    sp.run(['rm', os.path.join(pathname, 'sampled_npoints','sliceFibers')])
