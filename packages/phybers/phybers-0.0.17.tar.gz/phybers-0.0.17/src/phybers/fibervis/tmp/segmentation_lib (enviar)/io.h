/*io.h
Authors:  
    Narciso López López
    Andrea Vázquez Varela
Last modification: 24-10-2018
*/

#include <cstring>
#include <vector>
#include <fstream>
#include <sys/stat.h>

using namespace std;

/*Read .bundles files and return (by reference) a vector with the datas*/
void write_bundles(string subject_name, string output_path, vector<vector<float>> &assignment,vector<string> &names ,int ndata_fiber,
                vector<float> &subject_data);

/*Read .bundles files and return (by reference) a vector with the datas*/
vector<float> read_bundles(string path, unsigned short int ndata_fiber);

/*Get vector of bundles of the atlas*/
vector<float> get_atlas_bundles(string path, vector<string> names,unsigned short int ndata_fiber);

/*Read atlas information file*/
void read_atlas_info(string path, vector<string> &names, vector<unsigned char> &thres,
                unsigned int &nfibers_atlas, vector<unsigned int> &fibers_per_bundle);