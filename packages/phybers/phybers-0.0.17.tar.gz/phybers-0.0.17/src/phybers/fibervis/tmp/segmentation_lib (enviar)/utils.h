/*utils.h
Authors:  
    Narciso López López
    Andrea Vázquez Varela
Last modification: 24-10-2018
*/

#include <math.h>
#include <iostream>
#include <omp.h>

using namespace std;

float sqrt7(float x);

float euclidean_distance(float x1, float y1, float z1, float x2, float y2, float z2);

float euclidean_distance_norm(float x1, float y1, float z1, float x2, float y2, float z2);

char * str_to_char_array(string s);