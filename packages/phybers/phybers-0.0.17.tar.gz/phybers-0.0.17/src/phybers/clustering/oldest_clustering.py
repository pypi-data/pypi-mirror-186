import shlex
import sys
import os
from subprocess import run
from phybers.clustering.hclust.mainHClust import Hierarchical, Particional_Hierarchical, Write_Retrieve_clusters
from hclust.hierarchical import clusterTools as CT

def ffclust():

    pathname = os.path.dirname(__file__)
    cmd_str = "python3 " + os.path.join(pathname, "main.py ")
    print("cmd_str is: " + cmd_str)
    aux = 0

    for arg in sys.argv[1:]:
        if (aux == 1):
            print("Output path is: " + arg)
            outpath = arg
            aux = 0
        if(arg.startswith('--output-directory')):
            aux = 1

        cmd_str += arg + " "

    run(shlex.split(cmd_str))

#NEW HCLUST
def hclust_new(dir_raw_tractography='', result_path='', MaxDistance_Threshold='', maxdist='30', var = '3600'):
    
    """Execute Hierarchical Clustering
    """
    MatrixDist_output = os.path.join(result_path,"data","hierarch","matrixd.bin")
    affinities_graph_output = os.path.join(result_path,'data','hierarch','affin.txt')
    dendogram_output = os.path.join(result_path,'data','hierarch','dendogram.txt')
    partfile = os.path.join(result_path,'data','hierarch','particion_'+str(maxdist)+'.txt')
    
    Hierarchical(dir_raw_tractography,MatrixDist_output, affinities_graph_output,MaxDistance_Threshold,dendogram_output)
    Particional_Hierarchical(maxdist,var,dendogram_output,affinities_graph_output,partfile)
    wfv=CT.wforest_partition_maxdist_from_graph( dendogram_output,maxdist,True,affinities_graph_output,var)
    Write_Retrieve_clusters(result_path,wfv,dir_raw_tractography)

#OG HCLUST
def hclust(dir_raw_tractography='', MatrixDist_output='',
           affinities_graph_output ='',MaxDistance_Threshold='',dendogram_output='', maxdist='30', var = '3600',
           arbfile = '', afffile= '', partfile='', d_result='', wfv=''):
    
    """Execute Hierarchical Clustering
    """
    Hierarchical(dir_raw_tractography,MatrixDist_output, affinities_graph_output,MaxDistance_Threshold,dendogram_output)
    Particional_Hierarchical(maxdist,var,arbfile,afffile,partfile)
    wfv=CT.wforest_partition_maxdist_from_graph( arbfile,maxdist,True,afffile,var)
    Write_Retrieve_clusters(d_result,wfv,dir_raw_tractography)
