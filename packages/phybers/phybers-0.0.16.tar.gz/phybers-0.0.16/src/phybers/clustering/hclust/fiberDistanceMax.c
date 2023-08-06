//Author: Narciso Lopez Lopez

#include <stdio.h>
#include <stdlib.h>
#include "bundleTools.h"
#include "BundleTools.c"

int main(int argc, char *argv[]){

   if(argc!=3){
		printf("./fiberDistanceMax bundles distanceMatrix\n");
		printf("bundles: input file .bundles\n");
		printf("distanceMatrix: output file .bin with distance matrix\n");
		return -1;
	}

	struct bundle f1;
	f1 = read_bundle(argv[1]);

	float** m = (float**) malloc (f1.nfibers*sizeof(float*));

	m = fiberDistanceMax(f1);

	FILE *fw;
	fw = fopen(argv[2],"wb");

	int i,j,cont=1;
	for(i = 0; i<f1.nfibers; i++){
		for(j = 0; j<f1.nfibers; j++){
			if(j<cont){
				fprintf(fw, "%f\t",sqrt(*(m[i]+j)));
			}
			else{
				fprintf(fw, "%f\t",sqrt(*(m[j]+i)));
			}
			if(j==f1.nfibers-1){
				fprintf(fw, "\n");
			}
		}
		cont++;
	}

	fclose(fw);

   return 0;
}
