/* main.cpp
Authors:  
    Narciso López López
    Andrea Vázquez Varela
Last update: 24-10-2018 */

#include <iostream>
#include <omp.h>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <math.h>
#include <sys/stat.h>

using namespace std;

float sqrt7(float x){
    unsigned int i = *(unsigned int*) &x;
    i  += 127 << 23;	// adjust bias
    i >>= 1;	// approximation of square root
    return *(float*) &i;
}


float euclidean_distance(float x1, float y1, float z1, float x2, float y2, float z2){
    return ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2));
}

/*Calculate the euclidean distance between two 3d points normalized*/
float euclidean_distance_norm(float x1, float y1, float z1, float x2, float y2, float z2){
    return sqrt7((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2));
}

/*Return true when the fiber is discarded measuring the distance in central points*/
bool discard_center(vector<float> &subject_data, vector<float> &atlas_data,unsigned short int ndata_fiber,
 unsigned char threshold, unsigned int fiber_index, unsigned int fatlas_index){
    unsigned int fpoint = (fiber_index*ndata_fiber)+31; //Point of fiber, 31 is the middle of the fiber
    unsigned int apoint = (fatlas_index*ndata_fiber)+31; //Atlas point, 31 is the middle of the fiber

    float ed = euclidean_distance(subject_data[fpoint-1],subject_data[fpoint],subject_data[fpoint+1],
                                  atlas_data[apoint-1],atlas_data[apoint],atlas_data[apoint+1]);
    if (ed>(threshold*threshold)) return true;
    else return false;
}

bool discard_extremes(vector<float> &subject_data, vector<float> &atlas_data,unsigned short int ndata_fiber,
             unsigned char threshold, bool &is_inverted, unsigned int fiber_index, unsigned int fatlas_index){
    
    unsigned int fpoint1 = fiber_index*ndata_fiber;	//Point 0 of fiber
    unsigned int apoint1 = fatlas_index*ndata_fiber;	//Atlas point 0
    unsigned int fpoint21 = fpoint1+62;		//Last point on the fiber
    unsigned int apoint21 = apoint1+62;		//Last point on the fiber
    float first_points_ed_direct = euclidean_distance(subject_data[fpoint1], subject_data[fpoint1+1], subject_data[fpoint1+2],
                                                      atlas_data[apoint1], atlas_data[apoint1+1], atlas_data[apoint1+2]);
    float first_point_ed_flip = euclidean_distance(subject_data[fpoint1], subject_data[fpoint1+1], subject_data[fpoint1+2],
                                                   atlas_data[apoint21-2], atlas_data[apoint21-1], atlas_data[apoint21]);
    float first_points_ed = min(first_points_ed_direct, first_point_ed_flip);

    if (first_points_ed>(threshold*threshold)) return true;
    else{
        float last_points_ed;
        if (first_points_ed_direct<first_point_ed_flip) {
            is_inverted = false;
            last_points_ed = euclidean_distance(subject_data[fpoint21-2], subject_data[fpoint21-1], subject_data[fpoint21],
                                                atlas_data[apoint21-2], atlas_data[apoint21-1], atlas_data[apoint21]);
        }
        else {
            is_inverted = true;
            last_points_ed = euclidean_distance(subject_data[fpoint21-2], subject_data[fpoint21-1], subject_data[fpoint21],
                                                atlas_data[apoint1], atlas_data[apoint1+1], atlas_data[apoint1+2]);
        }
        if (last_points_ed>(threshold*threshold)) return true;
        else return false;
    }
}

bool discard_four_points(vector<float> &subject_data, vector<float> &atlas_data, unsigned short int ndata_fiber, unsigned char threshold, 
bool is_inverted, unsigned int fiber_index, unsigned int fatlas_index){
    vector<unsigned short int> points = {3,7,13,17};
    unsigned short int inv = points.size()-1;
    //#pragma parallel for
    for (unsigned int i = 0; i< points.size();i++){
        unsigned int point_fiber = (ndata_fiber*fiber_index) + (points[i]*3); //Mult by 3 dim
        unsigned int point_atlas = (ndata_fiber*fatlas_index)+ (points[i]*3);
        unsigned int point_inv_a = (ndata_fiber*fatlas_index)+ (points[inv]*3);
        float ed;
        if (!is_inverted){
            ed = euclidean_distance(subject_data[point_fiber],subject_data[point_fiber+1], subject_data[point_fiber+2],
                                    atlas_data[point_atlas],atlas_data[point_atlas+1], atlas_data[point_atlas+2]);}
        else{
            ed = euclidean_distance(subject_data[point_fiber],subject_data[point_fiber+1], subject_data[point_fiber+2],
                                    atlas_data[point_inv_a],atlas_data[point_inv_a+1], atlas_data[point_inv_a+2]);}

        if (ed>(threshold*threshold)) return true;
        inv--;
    }
    return false;
}

char * str_to_char_array(string s){
    int length = s.length()+1;
    char * char_array = new char[length];
#pragma omp parallel for
    for (unsigned short int i = 0; i<=length;i++){
        char_array[i] = s[i];
    }
    return char_array;
}

float discarded_21points (vector<float> &subject_data, vector<float> &atlas_data, unsigned short int ndata_fiber, 
                unsigned char threshold, bool is_inverted, unsigned int fiber_index, unsigned int fatlas_index){
    unsigned short int inv = 20;
    float ed;
    float max_ed = 0;
    for (unsigned short int i = 0; i<21; i++){
        unsigned int fiber_point = (ndata_fiber*fiber_index)+(i*3);
        unsigned int atlas_point = (ndata_fiber*fatlas_index)+(i*3);
        unsigned int point_inv = (ndata_fiber*fatlas_index)+(inv*3);
        if (!is_inverted){
            ed = euclidean_distance_norm(subject_data[fiber_point],subject_data[fiber_point+1], subject_data[fiber_point+2],
                                         atlas_data[atlas_point],atlas_data[atlas_point+1], atlas_data[atlas_point+2]);}
        else{
            ed = euclidean_distance_norm(subject_data[fiber_point],subject_data[fiber_point+1], subject_data[fiber_point+2],
                                         atlas_data[point_inv],atlas_data[point_inv+1], atlas_data[point_inv+2]);}

        if (ed>threshold) return -1;
        if (ed >= max_ed)
            max_ed = ed;
        inv--;
    }
    //After pass the comprobation of euclidean distance, will be tested with the lenght factor
    unsigned int fiber_pos = (ndata_fiber*fiber_index);
    unsigned int atlas_pos = (ndata_fiber*fatlas_index);
    float length_fiber1 = euclidean_distance_norm(subject_data[fiber_pos],subject_data[fiber_pos+1], subject_data[fiber_pos+2],
                                                  subject_data[fiber_pos+3],subject_data[fiber_pos+4], subject_data[fiber_pos+5]);
    float length_fiber2 = euclidean_distance_norm(atlas_data[atlas_pos],atlas_data[atlas_pos+1], atlas_data[atlas_pos+2],
                                                  atlas_data[atlas_pos+3],atlas_data[atlas_pos+4], atlas_data[atlas_pos+5]);
    float fact = length_fiber2 < length_fiber1 ? ((length_fiber1-length_fiber2)/length_fiber1) : ((length_fiber2-length_fiber1)/length_fiber2);
    fact = (((fact + 1.0f)*(fact + 1.0f))-1.0f);
    fact = fact < 0.0f ? 0.0f : fact;

    if ((max_ed+fact) >= threshold)
        return -1;
    else
        return max_ed;
}

/*Read .bundles files and return (by reference) a vector with the datas*/
void write_bundles(string subject_name, string output_path, vector<vector<float>> &assignment,vector<string> &names ,int ndata_fiber,
                   vector<float> &subject_data){
    int npoints = ndata_fiber/3;
    ofstream bundlesfile;
    struct stat sb;
    char * output_folder = str_to_char_array(output_path);
    if (stat(output_folder, &sb) == 0 && S_ISDIR(sb.st_mode)){
        char * command =  str_to_char_array("rm -r "+output_path);
        int del = system(command);
    }
    mkdir(output_folder);//, S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
    for (unsigned int i = 0; i<assignment.size();i++){
        if (assignment[i].size()!=0){
            string bundlesdata_path = output_path+"/"+subject_name+"_to_"+names[i]+".bundlesdata";
            char * bundlesdata_file = str_to_char_array(bundlesdata_path);
            FILE *fp = fopen(bundlesdata_file, "wb"); 	// Opening and writing .bundlesdata file.
            if (fp == NULL) {fputs ("File error opening .bundlesdata file\n",stderr); exit (1);}
            for (unsigned int j = 0; j < assignment[i].size(); j ++) {
                int fiber_index = assignment[i][j];
                fwrite(&npoints, sizeof(uint32_t),1, fp);
                fwrite(&subject_data[fiber_index*ndata_fiber], sizeof(float), ndata_fiber, fp);
            }
            fclose(fp);
            bundlesfile.open( output_path+"/"+subject_name+"_to_"+names[i]+".bundles", ios::out);
            bundlesfile<< "attributes = {"<<endl
                       <<"    \'binary\' : 1,"<<endl
                       <<"    \'bundles\' : [ '"<<(names[i])<<"', 0 ]," << endl
                       <<"    \'byte_order\' : \'DCBA\',"<<endl
                       <<"    \'curves_count\' : "<<assignment[i].size()<<","<< endl
                       <<"    \'data_file_name\' : \'*.bundlesdata\',"<<endl
                       <<"    \'format\' : \'bundles_1.0\',"<<endl
                       <<"    \'space_dimension\' : 3"<<endl
                       <<"  }"<<endl;
            bundlesfile.close();
            delete(bundlesdata_file);
        }
    }
    delete(output_folder);
}

/*Read .bundles files and return (by reference) a vector with the datas*/
vector<float> read_bundles(string path, unsigned short int ndata_fiber) {
    vector<float> data;
    char path2[path.length()+1];
    strncpy(path2, path.c_str(), sizeof(path2));
    path2[sizeof(path2) - 1] = 0;
    FILE *fp = fopen(path2, "rb");                      // Open subject file.
    if (fp == NULL) {fputs ("File error opening file\n",stderr); exit (1);}
    fseek (fp, 0 , SEEK_END);
    long lSize = ftell(fp);                                // Get file size.
    unsigned int sfiber = sizeof(uint32_t) + ndata_fiber*sizeof(float); // Size of a fiber (bytes).  // Add 1 element (uint32_t) because in .bundles/.bundlesdata format the first element of each fiber/centroid corresponds to the amount of points in the fiber/centroid. In this case that number should be always the same.
    float buffer [sfiber];
    unsigned int nFibers = lSize/(float)sfiber;                 // Number of fibers
    rewind(fp);
    for(unsigned int j = 0; j < (nFibers); ++j)    // Copy fibers.
    {
        int r = fread(buffer, sizeof(float), (ndata_fiber+1), fp);     // Skip the first element of each fiber/centroid (number of points).;
        if (r == -1)
            cout<<"error reading buffer data";
        for(int s = 1; s < ndata_fiber+1; ++s)
        {
            data.push_back(buffer[s]);
        }
    }

    fclose(fp);
    return data;
}

/*Get vector of bundles of the atlas*/
vector<float> get_atlas_bundles(string path, vector<string> names,unsigned short int ndata_fiber){
    vector<float> atlas_bundles;
    for (unsigned int i = 0; i<names.size();i++){
        string file_path = path + "/atlas_" +names[i] + ".bundlesdata";
        vector<float> bundle = read_bundles(file_path,ndata_fiber);
        atlas_bundles.insert( atlas_bundles.end(), bundle.begin(), bundle.end() );
    }
    return atlas_bundles;
}

/*Read atlas information file*/
void read_atlas_info(string path, vector<string> &names, vector<unsigned char> &thres,
                     unsigned int &nfibers_atlas, vector<unsigned int> &fibers_per_bundle){

    ifstream infile(path, ios::in );
    if( !infile )
        cerr << "Cant open " << endl;

    string name;
    unsigned short int t;
    unsigned int n;
    while (infile >> name >> t >> n)
    {
        names.push_back(name);
        thres.push_back(t);
        nfibers_atlas += n;
        fibers_per_bundle.push_back(n);
    }
}

vector<unsigned int> atlas_bundle(vector<unsigned int> &fibers_per_bundle, unsigned int nfibers){
    vector<unsigned int> correspondence(nfibers);
    unsigned int fiber_index = 0;
    for (unsigned int i = 0; i< fibers_per_bundle.size();i++){
        for (unsigned int j = 0; j<fibers_per_bundle[i];j++) {
            correspondence[fiber_index] = i;
            fiber_index++;
        }
    }
    return correspondence;
}

vector<unsigned char> parallel_segmentation(vector<float> &atlas_data, vector<float> &subject_data,
                                  unsigned short int ndata_fiber, vector<unsigned char> thresholds,
                                  vector<unsigned int> &bundle_of_fiber){
    unsigned int nfibers_subject = subject_data.size()/ndata_fiber;
    unsigned int nfibers_atlas = atlas_data.size()/ndata_fiber;
    vector<unsigned char> assignment(nfibers_subject,254);
    //vector<float> euclidean_distances(nfibers_subject,500.0);
    // unsigned int nunProc = omp_get_num_procs();
    unsigned int nunProc = omp_get_num_procs();
    omp_set_num_threads(nunProc);
#pragma omp parallel
    {

#pragma omp for schedule(auto) nowait
        for (unsigned long i = 0; i < nfibers_subject; i++) {
            float ed_i = 500;
            char assignment_i = 254;
            for (unsigned int j = 0; j < nfibers_atlas; j++) {
                bool is_inverted, is_discarded;
                float ed = -1;
                char b = bundle_of_fiber[j];
                //First test: discard_centers++; discard centroid

                is_discarded = discard_center(subject_data, atlas_data, ndata_fiber, thresholds[b], i, j);
                if (is_discarded) continue;

                //Second test: discard by the extremes
                is_discarded = discard_extremes(subject_data, atlas_data, ndata_fiber, thresholds[b], is_inverted, i, j);
                if (is_discarded) continue;

                //Third test: discard by four points
                is_discarded = discard_four_points(subject_data, atlas_data, ndata_fiber, thresholds[b], is_inverted, i, j);
                if (is_discarded) continue;

                ed = discarded_21points(subject_data, atlas_data, ndata_fiber, thresholds[b], is_inverted, i, j);
                if (ed != -1) {

                    if (ed < ed_i) {
                        ed_i = ed;
                        assignment_i = b;
                    }
                }
            }
            if (assignment_i!=254) {
                assignment[i]=assignment_i;
            }

        }
    }
    return assignment;
}

int main (int argc, char *argv[])
{
    double time_start, time_start_paralell, parallelFastCPUTime,final_time;
    time_start = omp_get_wtime();
    //Input data
    unsigned short int n_points = atoi(argv[1]);
    string subject_path = argv[2];
    string subject_name = argv[3];
    string atlas_path = argv[4];
    string atlas_inf = argv[5];
    string output_dir = argv[6];

    //Number of coord of each fiber
    unsigned short int ndata_fiber = n_points*3;

    //Atlas data
    vector<unsigned char> thresholds;
    vector<string> bundles_names;
    unsigned int nfibers_atlas = 0;
    vector<unsigned int> fibers_per_bundle;
    vector<unsigned int> bundle_of_fiber;
    vector<float> atlas_data;
    vector<vector<float>> atlas_centroids;

    //Subject data
    vector<float> subject_data;

    //Read the atlas information file and get the number of bundles of the atlas
    read_atlas_info(atlas_inf, bundles_names, thresholds, nfibers_atlas, fibers_per_bundle);
    //nbundles_atlas = bundles_names.size();
    bundle_of_fiber = atlas_bundle(fibers_per_bundle, nfibers_atlas);
    //Read the atlas data of .bundledata files and create the vectors of bundles
    atlas_data = get_atlas_bundles(atlas_path, bundles_names,ndata_fiber);
    subject_data = read_bundles(subject_path+"data", ndata_fiber);


    vector<unsigned char> assignment;
    time_start_paralell = omp_get_wtime();
    //for (int i = 0; i<5; i++)
    assignment = parallel_segmentation(atlas_data,subject_data,ndata_fiber,thresholds,bundle_of_fiber);
    parallelFastCPUTime = omp_get_wtime() - time_start_paralell;


    vector<vector<float>> map_results(bundles_names.size());
    //Map assignment
    for (unsigned int j = 0; j<assignment.size();j++) {
        if (assignment[j] != 254){
            map_results[assignment[j]].push_back(j);
        }
    }

    int count = 0;
    for (unsigned int i = 0; i<assignment.size();i++){
        if (assignment[i]!=254) {
            count++;
            // cout<<assignment[i]<<endl;
        }
    }
    printf("writing bundles\n");
    write_bundles(subject_name, output_dir, map_results,bundles_names ,ndata_fiber,subject_data);
    printf("finished writing bundles\n");
    final_time = omp_get_wtime() - time_start;
    cout<<"Total segmented fibers: "<< to_string(count)<<endl<<endl;
    cout<<"Execution time of fast algorithm (Parallel version): "<< parallelFastCPUTime<<endl;
    cout<<"Execution time IO operations: "<< final_time-parallelFastCPUTime<<endl;
    cout<<"Total time execution: "<<final_time<<endl;
    return 0;
}

