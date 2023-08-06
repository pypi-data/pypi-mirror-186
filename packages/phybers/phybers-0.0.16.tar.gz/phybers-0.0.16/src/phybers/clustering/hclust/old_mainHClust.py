#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Clustering Module
@author: liset
"""

import gc
import os
import sys
import time
import shlex
import numpy as np
import subprocess as sp
from . import clusterTools as CT
from . import read_write_bundle as rb
#from phybers.clustering.hclust import clusterTools as CT
#from phybers.clustering.hclust import read_write_bundle as rb



def Hierarchical(raw_tractography,MatrixDist_output, affinities_graph_output,MaxDistance_Threshold,dendogram_output):
    """
    Run to Hierarchical clustering.

    """
    pathname = os.path.dirname(__file__)
    #pathname = os.path.join(pathname, "hierarchical")
    sp.run(['mkdir','-p', os.path.join(MatrixDist_output, "data", "hierarch")])
    print('Hierarchical matrixdist: ')
    print(MatrixDist_output)
    
    if os.path.exists(os.path.join(pathname, "fiberDistanceMax")):
        #print("Found fibDist executable file. Erasing and compiling again.")
        sp.run(['rm', os.path.join(pathname, "fiberDistanceMax")])
        sp.run(['gcc', os.path.join(pathname, 'fiberDistanceMax.c'), '-o', os.path.join(pathname, 'fiberDistanceMax'), '-lm', '-w'])
    else:
        print("Executable file not found. Compiling fiberDistanceMax.c")
        sp.run(['gcc', os.path.join(pathname, 'fiberDistanceMax.c'), '-o', os.path.join(pathname, 'fiberDistanceMax'), '-lm', '-w'])
        if os.path.exists(os.path.join(pathname, "fiberDistanceMax")):
            print("fiberDistanceMax.c compiled.")
        else: 
            print("Executable file still not found. Exiting")
            exit()
            
    if os.path.exists(os.path.join(pathname, "getAffinityGraphFromDistanceMatrix")):
        #print("Found getAff executable file. Removing and compiling again.")
        sp.run(['rm', os.path.join(pathname, "getAffinityGraphFromDistanceMatrix")])
        sp.run(['g++', os.path.join(pathname, 'getAffinityGraphFromDistanceMatrix.cpp'), '-o', os.path.join(pathname, 'getAffinityGraphFromDistanceMatrix')])
    else:
        print("Executable file not found. Compiling getAffinityGraphFromDistanceMatrix.cpp")
        sp.run(['g++', os.path.join(pathname, 'getAffinityGraphFromDistanceMatrix.cpp'), '-o', os.path.join(pathname, 'getAffinityGraphFromDistanceMatrix')])
        if os.path.exists(os.path.join(pathname, "getAffinityGraphFromDistanceMatrix")):
            print("getAffinityGraphFromDistanceMatrix.cpp compiled.")
        else: 
            print("Executable file still not found. Exiting")
            exit()
            
    if os.path.exists(os.path.join(pathname, "getAverageLinkHCFromGraphFile")):
        #print("Found getAvrg executable file. Deleting and compiling again")
        sp.run(['rm', os.path.join(pathname, "getAverageLinkHCFromGraphFile")])
        sp.run(['g++', os.path.join(pathname, 'getAverageLinkHCFromGraphFile.cpp'), '-o', os.path.join(pathname, 'getAverageLinkHCFromGraphFile')])
    else:
        print("Executable file not found. Compiling getAverageLinkHCFromGraphFile.cpp")
        sp.run(['g++', os.path.join(pathname, 'getAverageLinkHCFromGraphFile.cpp'), '-o', os.path.join(pathname, 'getAverageLinkHCFromGraphFile')])
        if os.path.exists(os.path.join(pathname, "getAverageLinkHCFromGraphFile")):
            print("getAverageLinkHCFromGraphFile.cpp compiled.")
        else: 
            print("Executable file still not found. Exiting")
            exit()
    
    # Step1. Distance Matrix
    fiber_dir = os.path.join(pathname, "fiberDistanceMax")
    t0= time.time()
    #sp.run([os.path.join(pathname, "fiberDistanceMax"), raw_tractography, MatrixDist_output],check = True)
    #sp.run([fiber_dir, raw_tractography, MatrixDist_output],check = True)
    sp.call([os.path.join(pathname, "fiberDistanceMax"), raw_tractography, MatrixDist_output])
    print("Distance Matrix Delay: ", time.time()-t0, "[s]")

    # Step2. Affinities Graph
    t0= time.time()
    sp.run([os.path.join(pathname, "getAffinityGraphFromDistanceMatrix"), MatrixDist_output, affinities_graph_output, MaxDistance_Threshold])
    print("Affinities Graph Delay: ", time.time()-t0, "[s]")
    
    # Step3. Dendogram   
    t0= time.time()
    sp.run([os.path.join(pathname, "getAverageLinkHCFromGraphFile"),affinities_graph_output,dendogram_output])
    print("Dendogram Delay: ", time.time()-t0, "[s]")
    

def  Particional_Hierarchical(maxdist,var,arbfile,afffile,partfile):
    
    """
       Returns a ".txt" file with the detected clusters, where each list is a cluster.    
       maxdist, 30 or 40mmm is recommended
       var = 3600 ##minimum affinity within a cluster => #  N.exp( -max_cldist * max_cldist / var)
    """
    
    wfv=CT.wforest_partition_maxdist_from_graph( arbfile,maxdist,True,afffile,var)
    
    clusteres=wfv.clusters
        
    ar=open(partfile,'wt')
    ar.write(str(clusteres))
    ar.close()
    
def Write_Retrieve_clusters(d_result,wfv,dir_raw_tractography):

    """
    Function Retrieve clusters of fibers for Hierarchical clustering
    Return the clusters in the directory, d_result    
    """ 
    if not os.path.exists(d_result):
        os.mkdir(d_result)
    
    list_clusters=wfv.clusters
    
    raw_tractography = np.array(rb.read_bundle(dir_raw_tractography))
    
    for clus  in range(len(list_clusters)):
        if not os.path.exists(d_result+"/"):
            os.mkdir(d_result+"/")
            
        rb.write_bundle(d_result+"/"+str(clus)+".bundles",raw_tractography[list_clusters[clus]])



def cal_centroide(f):
    """
    Calculates the centroid for a set of fibers
    """
    cent=np.zeros_like(f[0])
    for i in range(len(f)):
        cent+=f[i]
    
    new_cent=cent/len(f) 
    
    return new_cent

