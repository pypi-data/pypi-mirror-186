"""The utils subpackage is a compendium of tools used for both the pre-processing of a tractography as well as for evaluating the performance of the clustering and the segmentation. It includes 4 modules:
    1) deform
    2) sampling
    3) intersection
    4) postprocessing
"""
import os
import sys
import numpy as N
import pandas as pd
import subprocess as sp
#from phybers.utils import FibersTools as fb
from . import FibersTools as fb
#import ffclust.FibersTools.FibersTools as fb

# AJUSTAR RUTAS

def deform(in_imgdef, indir, outdir): 
    """! Transforms a tractography file to another space using a non-linear deformation file. The inputs for the deform function are:
        
        <ol>
            <li>**in_imgdef**: Deformation image. Has to be a .nii file.</li>
            <li>**indir**: Fiber input file.</li>
            <li>**outdir**: Result directory path.</li>
        </ol>
    """
    pathname = os.path.dirname(__file__)
    def_path = os.path.join(pathname, 'deform')
    sys.path.insert(0,os.path.join(pathname,'deform'))
    
    if not in_imgdef.endswith('.nii'):
        print("You have to insert a .nii file as the first argument.")
        exit()

    if os.path.exists(os.path.join(pathname, 'deform','deform')):
        print("deform executable exists.")
    else:
        print("deform not found in path. Compiling it: ")
        print(pathname)
        sp.run(['gcc', 'main.c', '-o', 'deform', '-lm', '-w'], cwd = os.path.join(pathname, 'deform'), shell=True)
        #sp.Popen(['gcc', 'main.c', '-o', 'deform', '-lm', '-w'], cwd=def_path, shell=True)
        print(def_path)
        os.getcwd
        if os.path.exists(os.path.join(pathname, 'deform','deform')):
            print("deform executable has been created successfully.")
        else: 
            print("deform executable still not found. Exiting...")
            exit()


    print("Running deform...")
    
    sp.run(['./deform', in_imgdef, indir, outdir], cwd = os.path.join(pathname, 'deform'))
    #sp.Popen(['./deform', in_imgdef, indir, outdir],cwd = os.path.join(pathname,'deform'), shell=True)
        
def sampling(indir, in_npoints, outdir):
    """! Fiber sampling at n equidistant points. The inputs for the sampling function are:
        <ol>
            <li>**indir**: Fiber input file</li>
            <li>**in_npoints**: Number of points</li>
            <li>**outdir**: Result directory path.</li>
        </ol>
    """
    pathname = os.path.dirname(__file__)
    sys.path.insert(0,os.path.join(pathname,'sampling'))


    if os.path.exists(os.path.join(pathname, 'sampling','sliceFibers')):
        print("sliceFibers exists.")
    else:
        print("dbindex does not exist in path. Compiling it: ")
        sp.run(['gcc', 'sliceFibers.c', '-o', 'sliceFibers', '-lm', '-w'],cwd=os.path.join(pathname,'sampling'))
        
        if os.path.exists(os.path.join(pathname, 'sampling','sliceFibers')):
            print("Target directory has been created successfully.")

        else: 
            print("Target directory still doesn't exist. Exiting...")
            exit()
    
    sp.run([ './sliceFibers', indir, outdir, in_npoints], check = True, cwd=os.path.join(pathname,'sampling'))
    
    
def inter2bundles(dir_fib1,dir_fib2,outdir, d_th):
    """! Calculates a similarity measure between two sets of brain fibers (fiber clusters or segmented bundles). The inputs for the intersection function are:
        <ol>
            <li>**dir_fib1**: First bundle file.</li>
            <li>**dir_fib2**: Second bundle file.</li>
            <li>**outdir**: Result directory path.</li>
            <li>**d_th**: TH_Dmax</li>
        </ol>
    """
    pathname = os.path.dirname(__file__)
    sys.path.insert(0,os.path.join(pathname,'intersection'))
    
    if os.path.exists(os.path.join(pathname,'intersection','fiberDistanceMax2bun')):
        print("Executable found.")
    else:
        print("Executable not found in path. Compiling it: ")
        #sp.run(['gcc', pathname + '/dinter/fiberDistanceMax2bun.c', '-o', pathname + '/dinter/fiberDistanceMax2bun', '-lm'])
        sp.run(['gcc', 'fiberDistanceMax2bun.c', '-o', 'fiberDistanceMax2bun', '-lm'], check = True, 
        cwd = os.path.join(pathname,'intersection'))
        #AÑADIR CWD = pathname, hacer tal cual hclust
        if os.path.exists(os.path.join(pathname,'intersection','fiberDistanceMax2bun')):
            print("Executable has been created successfully.")

        else:
            print("Executable still not found. Exiting...")
            exit()


    # Name de los conjuntos de fibras a comprar
    labelsb1 = os.path.split(dir_fib1)[1] # name of fiber set 1 (m rows)    
    labelsb2= os.path.split(dir_fib2)[1]  # name of fiber set 2 (n columns)

    
    p1=0 # constantes para guardar los porcentajes de intersección del input 1
    p2=0 # constantes para guardar los porcentajes de intersección del input 2

    for b1 in labelsb1: 
        for b2 in labelsb2:
            
            str_out=b1.split('.')[0]+'-'+b2.split('.')[0] # Construyendo nombre para la matriz de intersección.
                  
            outfile=outdir+str_out+'.txt'
            
            
            # Sie ejecuta el script en C que calcula la distancia euclidiana entre dos bundles.
            
            #sp.run([ pathname + '/dinter/fiberDistanceMax2bun', dir_fib1, dir_fib2, outfile])
            sp.run(['./fiberDistanceMax2bun', dir_fib1, dir_fib2, outfile],cwd=os.path.join(pathname,'intersection'))
    
            ar=open(outfile,'rt')
            t=ar.readlines();ar.close()
            m=len(t) # m > num de filas
            n=len(t[0].split('\t')[:-1]) # num > num columnas
            
            M = N.zeros((m,n),dtype = 'float32')
            
            for i in range(m):
                fila=t[i][:-1].split('\t')[:-1]
                for j in range(n):
                    M[i,j]=float(fila[j])
            
            F_under_th=N.where( M < d_th) # fibers with at least 1 other fiber has distance under the threshold
            xp1=list(set(F_under_th[0]))
            yp2=list(set(F_under_th[1]))
            
    
            
            p1=(len(xp1)/fb.getBundleSize(dir_fib1))*100#porcentaje b1
            p2=(len(yp2)/fb.getBundleSize(dir_fib2))*100#porcentaje b2
            
            return (p1,p2)


  

    
def postprocessing(in_directory):
    ##THIS IS THE DOC WAAAA
    #
    """! Contains a set of algorithms that are applied on the results of clustering and segmentation algorithms.
        1) Fibers Lens (se calcula para el centroide del clúster)
        2) Fibers Size ( cantidad de fibras por clúster)
        3) Distancia intra-clúster mínima,  Distancia intra promedio y  Distancia intra máxima
        4) Rij
        5) DBindex
        
        <ol>
            <li>**in_directory**: Flies directory path.</li>
        </ol>
    """
    pathname = os.path.dirname(__file__)
    
    in_centroides=os.path.join(in_directory,'FinalCentroids','centroids.bundles')
    in_clusters_directory=os.path.join(in_directory,'FinalBundles')
        
    stadisticsFolder =  os.path.join(in_directory, "stadistics")
    
    if not os.path.exists(in_directory):
        os.makedirs(in_directory)
    
    if not os.path.exists(stadisticsFolder):
        os.makedirs(stadisticsFolder)

    # Fibers Lens and Fibers Size 
    txt_lens = ""
    txt_sizes = ""
        
#    stadisticsFolder =  os.path.join(in_directory, "stadistics")
    print(stadisticsFolder)
        
    if not os.path.exists(in_directory):
        os.makedirs(in_directory)
    if not os.path.exists(in_directory):
        os.makedirs(in_directory)
    centroides=fb.read_bundle(in_centroides)        
    for i in range(len(centroides)):
        txt_lens += str(fb.fiber_lens(centroides[i]))+"\n"         
        txt_sizes += str(fb.getBundleSize(in_clusters_directory+'/'+str(i)+".bundles"))+"\n"
            
    with open(os.path.join(stadisticsFolder, "lens.txt"), "w") as file:
        file.write(txt_lens)
        
    with open(os.path.join(stadisticsFolder, "sizes.txt"), "w") as file:
        file.write(txt_sizes)
   
    # - Distancia intra-clúster mínima, Distancia intra promedio, Rij y DBindex

    dbindex_path = os.path.join(pathname, 'dbindex')
    sys.path.insert(0,os.path.join(pathname,'dbindex'))


#    sp.run(['g++','-std=c++14','-O3', 'dbindex.cpp', '-o', 'dbindex', '-fopenmp', '-ffast-math'],
#        cwd = dbindex_path)
        
            
    sp.run([ './dbindex',in_centroides, in_clusters_directory, os.path.join(stadisticsFolder,'mensure'),'21'], cwd = dbindex_path)
    
    # Dataframe
    fb.Stadistics_txt_toxlsx(stadisticsFolder) 
    
    return pd.read_excel(stadisticsFolder+'/stadistics.xlsx') 



#%%
# Luego, aplicar múltiples filtrados se reduce a la utilización de las herramientas para filtrar objetos pandas
# Ejemplo de filtrado por el tamaño




def write_bundle( outfile, points ):
    """! Write bundles File.
    """
    #write bundles file
    f = open( outfile + 'data','wb')
    ncount = len( points )
    for i in range( ncount ):
        f.write(N.array( [ len( points[ i ] ) ], N.int32 ).tostring() )
        f.write( points[ i ].ravel().tostring() )
    
    f.close()
  # write minf file
    minf = """attributes = {\n    'binary' : 1,\n    'bundles' : %s,\n    'byte_order' : 'DCBA',\n    'curves_count' : %s,\n    'data_file_name' : '*.bundlesdata',\n    'format' : 'bundles_1.0',\n    'space_dimension' : 3\n  }"""
    open( outfile, 'w' ).write(minf % ( [ 'points', 0 ], ncount ) )
  
def read_bundle( infile ):
    """! Read Bundles File.
    """
    points = []
    bun_file = infile + 'data'
    os.path.getsize( bun_file )
    bytes = os.path.getsize( bun_file )
    num = bytes / 4

    num_count = 0
    f = open( bun_file , 'rb')
    while num_count < num:
        p = N.frombuffer( f.read( 4 ), dtype=N.int32 )[ 0 ] # numero de puntos de la fibra
        vertex = N.frombuffer( f.read( p * 3 * 4 ), dtype=N.float32 ).reshape( -1, 3 ) # lee coordenadas fibra
        points.append( vertex )
        num_count = num_count + 1 + ( p * 3 )

    f.close()

    return points
