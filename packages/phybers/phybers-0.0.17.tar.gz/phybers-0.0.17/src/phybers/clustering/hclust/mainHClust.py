#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Clustering Module
@author: liset
"""


#import read_write_bundle as rb
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

def hierarchical(fiber_input,outfile_dir,MaxDistance_Threshold):
    """
    Run to Hierarchical clustering.

    """
    #./hclust/fiberDistanceMax
    pathname = os.path.dirname(__file__)
    print(pathname)
    
    MatrixDist_output = os.path.join(outfile_dir, 'matrixd.bin')
    affinities_graph_output = os.path.join(outfile_dir,'affin.txt')
    dendogram_output = os.path.join(outfile_dir,'dendogram.txt')
    
    if os.name == 'nt': #This will run if OS = Windows
        print('Windows')
        
        # Step1. Distance Matrix
        t0 = time.time()
        sp.run(['./fiberDistanceMax', fiber_input, MatrixDist_output], check = True, cwd=pathname)
        gc.collect()
        print("Distance Matrix Delay: ", time.time()-t0, "[s]")

        # Step2. Affinities Graph
        t0= time.time()
        sp.run(['./getAffinityGraphFromDistanceMatrix', MatrixDist_output, affinities_graph_output, MaxDistance_Threshold], check = True, cwd=pathname)
        gc.collect()
        print("Affinities Graph Delay: ", time.time()-t0, "[s]")
    
        # Step3. Dendogram   
        t0= time.time()
        sp.run(['./getAverageLinkHCFromGraphFile',affinities_graph_output,dendogram_output], check = True, cwd=pathname)
        gc.collect()
        print("Dendogram Delay: ", time.time()-t0, "[s]")

    elif os.name == 'posix': #This will run if OS = Linux
        print('Linux')
    
        # Step1. Distance Matrix
        t0 = time.time()
        sp.run(['./fiberDistanceMax', fiber_input, MatrixDist_output], check = True, cwd=pathname)
        gc.collect()
        print("Distance Matrix Delay: ", time.time()-t0, "[s]")

        # Step2. Affinities Graph
        t0= time.time()
        sp.run(['./getAffinityGraphFromDistanceMatrix', MatrixDist_output, affinities_graph_output, MaxDistance_Threshold], check = True, cwd=pathname)
        gc.collect()
        print("Affinities Graph Delay: ", time.time()-t0, "[s]")
        
        # Step3. Dendogram   
        t0= time.time()
        sp.run(['./getAverageLinkHCFromGraphFile',affinities_graph_output,dendogram_output], check = True, cwd=pathname)
        gc.collect()
        print("Dendogram Delay: ", time.time()-t0, "[s]")    




#%% Function and Example Particional Hierarchical Clustering

def  particional_hierarchical(fiber_input, outfile_dir, PartDistance_Threshold,var,final_bundles_dir):
    
    """Writes the cluster bundles (bundles format) and fiber indexes per cluster (file '.txt')
       Allow tree partitioning using:
       PartDistance_Threshold = 30 or 40mm (recommended) and  
       var = 3600 (recommended) minimum affinity within a cluster => #  N.exp( -max_cldist * max_cldist / var)      
    """
    
    arbfile = os.path.join(outfile_dir, 'dendogram.txt')
    afffile = os.path.join(outfile_dir, 'affin.txt')
    partfile = os.path.join(outfile_dir, 'index_fiberscluster.txt')
    
    t0= time.time()
    wfv=CT.wforest_partition_maxdist_from_graph(arbfile,PartDistance_Threshold,True,afffile,var)
    
    clusteres=wfv.clusters
        
    ar=open(partfile,'wt')
    ar.write(str(clusteres))
    ar.close()
    
    tractography = np.array(rb.read_bundle(fiber_input))
    
    for clus  in range(len(clusteres)):    
            
        rb.write_bundle(final_bundles_dir+"/"+str(clus)+".bundles",tractography[clusteres[clus]])
    
    print("Particional Hierarchical Delay: ", time.time()-t0, "[s]")

