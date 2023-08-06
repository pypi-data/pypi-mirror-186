import os
import sys
import shlex
import subprocess as sp

#in_imgdef="data/100206/acpc_dc2standard.nii" #importante, dar error si no se entrega
#indir="data/100206/100206.bundles" #importante
#outdir="data/100206/100206_MNI.bundles"
#sp.run(['./deformHCPtoMNI/deform',in_imgdef, indir, outdir])

def deform(in_imgdef, indir, outdir):

    pathname = os.path.dirname(__file__)
    
    if not in_imgdef.endswith('.nii'):
        print("You have to insert a .nii file as the first argument.")
        exit()

    if os.path.exists(pathname + 'deform/deformHCPtoMNI/deform'):
        print("deform executable exists.")
    else:
        print("deform not found in path. Compiling it: ")
        sp.run(['gcc', pathname + 'deform/deformHCPtoMNI/main.c', '-o', pathname + 'deform/deformHCPtoMNI/deform', '-lm', '-w'])
        
        if os.path.exists(pathname + 'deform/deformHCPtoMNI/deform'):
            print("deform executable has been created successfully.")
        else: 
            print("deform executable still not found. Exiting...")
            exit()


    print("Running deform...")
    sp.run([pathname + 'deform/deformHCPtoMNI/deform', in_imgdef, indir, outdir])
