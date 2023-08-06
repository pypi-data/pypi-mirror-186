##
# @mainpage Segmentation module
# @brief Segmentation of neural fibers based on a multi-subject atlas. This algorithm has the objective of classifying the subject fibers according to a multi-subject fascicle atlas. To classify the fibers of a subject, it utilizes the maximum euclidian distance between each subject fibers and each atlas centroid, keeping only the fibers with a distance below a defined threshold for each atlas fascicle.
#Segmentación de fibras cerebrales basado en atlas multisujeto. Este algoritmo tiene el objetivo de clasificar las fibras de los sujetos en función de un atlas de fascículos multisujeto. Para clasificar las fibras de un sujeto se utiliza la máxima distancia Euclidiana entre cada fibra del sujeto y cada centroide del atlas, manteniendo solamente las fibras con una distancia por debajo de un umbral definido para cada fascículo del atlas.
# \tableofcontents
# @subsection description_main How to run
# The segmentation module is executed by running the following on console:
#
# > ```python3 -m segmentation <npoints> <fibrasdir> <idsubj> <atlasdir> <atlasInformation> <result_path>```
# Donde la definición de cada argumento se puede encontrar en el siguiente enlace: \ref segmentation.main
# Where each argument's definition can be found in the following link: \ref segmentation.main
#
#
import os
import sys
from pathlib import Path
from subprocess import run


#Global Constants
## Absolute path of this file.
pathname = os.path.dirname(__file__)
## Number of points.
npoints = sys.argv[1]
## Fibers .bundles path.
fibrasdir = sys.argv[2]
## Subject ID.
idsubj = sys.argv[3]
## Atlas directory path.
atlasdir = sys.argv[4]
## Atlas info file.
atlasInformation = sys.argv[5]
## Output directory path for the segmentated fascicles for the subject.
result_path = sys.argv[6]

aux = str(Path(result_path).parents[0])

if os.path.exists(result_path):
    print("Target directory exists.")

else:
    print("Target directory does not exist in path. Creating it: ")
    # run(['mkdir', aux + '/result'])
    
    if os.name == 'nt':
        os.system('mkdir ' + os.path.join(aux,'result'))
        print("Windows pogger creating result")
    elif osname == 'posix':
        run(['mkdir', os.path.join(aux,'result')])

    if os.path.exists(result_path):
        print("Target directory has been created successfully.")

    else: 
        print("Target directory still doesn't exist. Exiting...")
        exit()

seg_result = os.path.join(result_path, "seg_bundles")

if os.name == 'nt':
    os.system('mkdir ' + seg_result)

elif os.name == 'posix':
    run(['mkdir', seg_result])

id_seg_result = os.path.join(result_path, "id_txt_seg")


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
        run(['g++','-std=c++14','-O3', pathname + '/main.cpp', '-o', pathname + '/main.o', '-fopenmp', '-ffast-math'])
        
        if os.path.exists(os.path.join(pathname, "main.o")):
            print("main.cpp compiled. Running executable file: ")
        else:
            print("Executable file still not found. Exiting")
            exit()
    run([os.path.join(pathname, "./main.o"), npoints, fibrasdir, idsubj, atlasdir, atlasInformation, seg_result, id_seg_result])


print("Result is in: " + result_path)

