"""! @brief Testing"""
##
# @mainpage Fibers segmentation wrapper
#
# @section description_main Description
# An example of the segmentation code for fibers.
#
# @brief Example Python program with Doxygen style comments.
#
#Imports
import os
import sys
import numpy as np
from pathlib import Path
from subprocess import run
#import read_write_bundle as rb
#from phybers.segment import read_write_bundle as rb
from .segment import read_write_bundle as rb

def fiberseg(npoints, fiber_input, idsubj, atlasdir, atlasInformation, result_path):
    
    pathname = os.path.dirname(__file__)
    aux = str(Path(result_path).parents[0])
    
    if os.path.exists(result_path):
        print("Target directory exists.")

    else:
        print("Target directory does not exist in path. Creating it: ")
        # run(['mkdir', aux + '/result'])
        
        if os.name == 'nt':
            os.system('mkdir ' + os.path.join(aux,'result'))
            print("Windows pogger creating result")
        
        elif os.name == 'posix':
            #run(['mkdir', os.path.join(aux,'result')])
            os.makedirs(os.path.join(aux,'result'))

        if os.path.exists(result_path):
            print("Target directory has been created successfully.")

        else: 
            print("Target directory still doesn't exist. Exiting...")
            exit()

#    seg_result = os.path.join(result_path, "seg_bundles")
#
#    if os.name == 'nt':
#        os.system('mkdir ' + seg_result)
#
#    elif os.name == 'posix':
#        run(['mkdir', seg_result])
#
#    id_seg_result = os.path.join(result_path, "id_txt_seg")

# Agregando inicio
    seg_result = result_path + '/FinalBundles21p'
    os.makedirs(seg_result, exist_ok=True)
    
    id_seg_result= result_path + '/idx_bundles'
    os.makedirs(id_seg_result, exist_ok=True)

    final_bundles_dir = result_path + '/FinalBundles'
    os.makedirs(final_bundles_dir, exist_ok=True)
    
    final_centroids_dir = result_path + '/FinalCentroids'    
    os.makedirs(final_centroids_dir, exist_ok=True)
    
    outfile_dir= result_path + '/outfile' 
    os.makedirs(outfile_dir, exist_ok=True)
    
    fibrasdir = os.path.join(outfile_dir,'whole_brain21p.bundles')   
    
    
    run([os.path.join(pathname, 'fiberseg','sliceFibers'), fiber_input, fibrasdir,'21']) 
# agregado Fin

    ## Output directory path for the index of the original fibers for each detected fascicle.

    #Functions
     
    if os.name == 'nt':
        if os.path.exists(os.path.join(pathname, "main_minGW.o")):
            print("Found executable file. Running segmentation executable file: ")
        else:
            print("Executable file not found. Compiling main.cpp")
            os.system('g++ ' + '-std=c++14 ' + '-O3 ' +  os.path.join(pathname, 'main_minGW.cpp') + ' -o '+ os.path.join(pathname, 'main_minGW.o') + ' -fopenmp ' + '-ffast-math')
            
            if os.path.exists(os.path.join(pathname, "main_minGW.o")):
                print("main.cpp compiled. Running executable file: ")
            else: 
                print("Executable file still not found. Exiting")
                exit()
        os.system(os.path.join(pathname, "./main_minGW.o") + " " + npoints + " " +  fibrasdir + " " + idsubj + " " + atlasdir + " " + atlasInformation + " " + seg_result + " " + id_seg_result)

    
    elif os.name == 'posix':
        if os.path.exists(os.path.join(pathname, "main.o")):
            print("Found executable file. Running segmentation executable file: ")
        else:
            print("Executable file not found. Compiling main.cpp")
            run(['g++','-std=c++14','-O3', pathname + '/fiberseg/main.cpp', '-o', pathname + '/main.o', '-fopenmp', '-ffast-math'])
            
            if os.path.exists(os.path.join(pathname, "main.o")):
                print("main.cpp compiled. Running executable file: ")
            else: 
                print("Executable file still not found. Exiting")
                exit()
                
        run([os.path.join(pathname, "./fiberseg/main.o"), npoints, fibrasdir, idsubj, atlasdir, atlasInformation, seg_result, id_seg_result])

### Agregado inicio
    tract= rb.read_bundle(fiber_input)
    for i in os.listdir(id_seg_result):
        index=[]    
        with open (os.path.join(id_seg_result,i)) as file:
            for line in file:
                index.append(int(float(line[:-2])))   
        
        bun=np.array(tract, dtype='object')[index]
        rb.write_bundle(os.path.join(final_bundles_dir,idsubj+'_to_'+i[:-4]+'.bundles'), bun)
### fin
                    
    print("Result is in: " + result_path)
    

#############################################################################################


#def segroi(**args):
