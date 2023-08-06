/*setmentation.h
Authors:  
    Narciso López López
    Andrea Vázquez Varela
Last modification: 24-10-2018
*/

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdio>
#include <algorithm>
#include "io.h"
#include "utils.h"

using namespace std;

struct Result {
  float *euclidean_distances;
  string *names;
};

/*Return true when the fiber is discarded measuring the distance in central points*/
bool discard_center(vector<float> &subject_data, vector<float> &atlas_data,unsigned short int ndata_fiber, 
          unsigned char threshold, unsigned int fiber_index, unsigned int fatlas_index);

bool discard_extremes(vector<float> &subject_data, vector<float> &atlas_data,unsigned short int ndata_fiber,
          unsigned char threshold, bool &is_inverted, unsigned int fiber_index, unsigned int fatlas_index);

bool discard_four_points(vector<float> &subject_data, vector<float> &atlas_data, unsigned short int ndata_fiber, unsigned char threshold, 
          bool is_inverted, unsigned int fiber_index, unsigned int fatlas_index);

float discarded_21points (vector<float> &subject_data, vector<float> &atlas_data, unsigned short int ndata_fiber, 
          unsigned char threshold, bool is_inverted, unsigned int fiber_index, unsigned int fatlas_index); 

vector<unsigned int> atlas_bundle(vector<unsigned int> &fibers_per_bundle, unsigned int nfibers);

string * get_names_assignment(vector<unsigned char> &assignment, vector<string> &bundles_names);

void freeme(struct Result results);

vector<unsigned char> parallel_segmentation(vector<float> &atlas_data, vector<float> &subject_data,
          vector<float> &euclidean_distances, unsigned short int ndata_fiber, vector<unsigned char> thresholds,
          vector<unsigned int> &bundle_of_fiber);


/*Input:
n_points: Number of points of fiber. Example: 21
subject_path: Bundles file. Example: subject.bundles
subject_name: Subject name. Example: sujeto1
atlas_path: Bundles directory of the atlas. Example: Atlas_claudio/bundles/
atlas_inf: Atlas information file. Example: Atlas_Claudio/atlas_information_file.txt
output_directory: Name of the output directory. Example: results

Output:
*Dynamic vector of pointers with size = 2. The first pointer points to the euclidean distances dynamic vector and the 
second pointer points to the names of the bundles. For example:
result_vector: [pointer1, pointer2]
vector of pointer 1: [2.5,  3.4,  5.5]
vector of pointer 2: [CC,   AR,   PRE]
Mean:
Fiber 0: Minimum euclidean distance with CC is 2.5
Fiber 1: Minimum euclidean distance with AR is 3.4
Fiber 2: Minimum euclidean distance with PRE is 5.5
*/
struct Result segmentation(unsigned short int n_points, string subject_path, 
          string subject_name, string atlas_path, string atlas_inf, string output_dir);