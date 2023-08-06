#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

#include "nifti1.h"
#include "bundleTools.h"
#include "BundleTools.c"

#define MIN_HEADER_SIZE 348

int main(int argc, char *argv[])
{

    if(argc <= 3){
        printf("Argumentos incorrectos! Se debe escribir \\.deform.exe acpc_dc2standard.nii dir_fibras.bundles dir_fibras_deform.bundles");
        exit(1);
    }
    //Leo el volumen .nii
    nifti_1_header atlas;
    int ret;
    FILE *fp;
   // fp = fopen("100206/MNINonLinear/xfms/acpc_dc2standard.nii", "rb");

    //fp = fopen("F:/subject_100408/100408_transf/MNINonLinear/xfms/acpc_dc2standard.nii", "rb");
    fp = fopen(argv[1], "rb");

    ret = fread(&atlas, MIN_HEADER_SIZE, 1, fp);

    printf("size_x: %d , size_y: %d , size_z: %d, size_dim: %d\n", atlas.dim[1], atlas.dim[2], atlas.dim[3],atlas.dim[4]);
    printf("voxel_size_x: %f , voxel_size_y: %f , voxel_size_z: %f, voxel_size_dim: %f\n\n", atlas.pixdim[3], atlas.pixdim[1], atlas.pixdim[2], atlas.pixdim[4]);
    printf("Voxel offset: %f\n", atlas.vox_offset);
    printf("Verificacion slope: %f\n", atlas.scl_slope);

    ret = fseek(fp, (long)(atlas.vox_offset), SEEK_SET);

    float *data=NULL;
    data = (float *) malloc(sizeof(float) * atlas.dim[3]*atlas.dim[1]*atlas.dim[2]*atlas.dim[4]);
    ret = fread(data, sizeof(float), atlas.dim[3]*atlas.dim[1]*atlas.dim[2]*atlas.dim[4], fp);
    //free(data);
    if(atlas.dim[3]*atlas.dim[1]*atlas.dim[2]*atlas.dim[4] == ret){
        // THIS IS THE PROBLEM
        printf("Se hizo la lectura de todos los voxel: ret %i    data_size %i\n", ret,atlas.dim[3]*atlas.dim[1]*atlas.dim[2]*atlas.dim[4]);
        //free(ret);
        printf("death 0");
        }
    else{
        printf("Error al leer los voxel del atlas ret %i    data_size %i\n", ret,atlas.dim[3]*atlas.dim[1]*atlas.dim[2]*atlas.dim[4]);
        exit(1);
        }
    fclose(fp);
    printf("death 1");
   // printf("Value data: %f\n", data[1]);

//    printf("Value data: %i\n", data[1870152]);

    for(int i = 0; i < atlas.dim[3]*atlas.dim[1]*atlas.dim[2]*atlas.dim[4]; i++){

        if(data[i]==1.0){
        printf("Value data: %i index %i\n", data[i],i);

        }
    }

   // int ind = index_by_coord(4, 4, 6, 1, atlas.dim[1], atlas.dim[2],atlas.dim[3],atlas.dim[4] );
   // printf("Value data index: %i Value data: %f\n", ind, data[ind]);

    //Leo las fibras
    struct bundle all_centroides, all_fibras, aux_c1, aux_c2, centroides, aux_f1, aux_f2, fibras;
    //all_centroides = read_bundle(argv[2]);

    //all_fibras = read_bundle("F:/subject_100408/100408/T1w/Diffusion/100408_tk.bundles");

    all_fibras = read_bundle(argv[2]);

    int fi = all_fibras.nfibers;
    printf("Fibras totales leidas: %i\n", fi);

    //Creo el nuevo bundles donde se guardará la transformación
    float** points; // puntero a cada fibra
    points = (float**) malloc (all_fibras.nfibers*sizeof(float*));

    int32_t* npoints;//Puntero para la cantidad de puntos de cada fibra
    npoints=(int32_t*) malloc(all_fibras.nfibers*sizeof(int32_t));//Memoria para cada fibra


    struct bundle fas;

    fas.npoints=npoints;
    fas.points=points;
    fas.nfibers = all_fibras.nfibers;



    for(int i = 0; i < all_fibras.nfibers; i++){

        fas.npoints[i] = all_fibras.npoints[i];
        fas.points[i] = (float* )malloc((*(all_fibras.npoints+i))*3*sizeof(float));
        //fas.points[i] = all_fibras.points[i];
        }

    for(int i=0;i<(all_fibras.nfibers);i++) //itero por todas las fibras
    {

        for(int k=0;k<(all_fibras.npoints[i]);k++) //Itero por los puntos de cada fibra
        {
            int x =      (int)(*(all_fibras.points[i]+(k*3)+0))/2;
            int y = 108- (int)(*(all_fibras.points[i]+(k*3)+1))/2;
            int z = 90 - (int)(*(all_fibras.points[i]+(k*3)+2))/2;

            int coord_0 = index_by_coord( x,  y,  z,  0, atlas.dim[1], atlas.dim[2],atlas.dim[3],atlas.dim[4]);
            int coord_1 = index_by_coord( x,  y,  z,  1, atlas.dim[1], atlas.dim[2],atlas.dim[3],atlas.dim[4]);
            int coord_2 = index_by_coord( x,  y,  z,  2, atlas.dim[1], atlas.dim[2],atlas.dim[3],atlas.dim[4]);

            float traslation_0 = data[coord_0];
            float traslation_1 = data[coord_1];
            float traslation_2 = data[coord_2];
            //printf("%i   %i    %i \n", x, y, z);
           // printf("%f   %f    %f \n", all_fibras.points[i][k*3+0], all_fibras.points[i][k*3+1], all_fibras.points[i][k*3+2]);

        //printf("%i\n", k);
        //fas.points[i][k]=all_fibras.points[i][k];
        *(fas.points[i]+(k*3)+0) = *(all_fibras.points[i]+(k*3)+0) - traslation_0;
        *(fas.points[i]+(k*3)+1) = *(all_fibras.points[i]+(k*3)+1) + traslation_1;
        *(fas.points[i]+(k*3)+2) = *(all_fibras.points[i]+(k*3)+2) + traslation_2;
        //fas.points[i][k*3+0]=all_fibras.points[i][k*3+0];
        /*fas.points[i][k*3+0]=all_fibras.points[i][k*3+1];
        fas.points[i][k*3+0]=all_fibras.points[i][k*3+2];*/
        }
    }

       write_bundle(argv[3], fas.nfibers, fas.npoints, fas.points);


/*
    for(int i = 0; i < all_fibras.nfibers; i++){

        fas.npoints[i] = all_fibras.npoints[i];
        fas.points[i] = (float* )malloc((*(all_fibras.npoints+i))*3*sizeof(float));
        fas.points[i] = all_fibras.points[i];
        }

    write_bundle("101309_fas_test.bundles", fas.nfibers, fas.npoints, fas.points);*/

/*
    for(int i = 0; i < all_fibras.nfibers; i++)
        {
            int aux = all_fibras.npoints[i];
            int j=0;



            printf("%f   %f    %f \n", all_fibras.points[i][0]);
        }


            int i = 1;
            int aux = all_fibras.npoints[i];
            int j=0;
*/


            //printf("%f   %f    %f \n", all_fibras.points[0][0], all_fibras.points[0][3], all_fibras.points[0][6]);






    return 0;
}


int index_by_coord(int x, int y, int z, int w, int dimx, int dimy,int dimz,int dimw){



    return x + y*dimx + z* dimx*dimy + w* dimx*dimy*dimz;
}
