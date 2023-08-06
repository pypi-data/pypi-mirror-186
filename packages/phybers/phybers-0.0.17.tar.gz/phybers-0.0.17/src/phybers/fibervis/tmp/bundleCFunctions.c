#include "stdio.h"
#include "math.h"
#include <GL/gl.h>
#include <stdbool.h>
#include "ROISegmentationCFunctions.h"


// C function for fast read of bundle files
void readBundleFile(char * filePath, 
	void * pyPositions, 
	void * pyNormals, 
	void * pyColors, 
	void * pyEbo, 
	void * pyFiberSize, 
	void * pyBundleStart, 
	int curvesCount, 
	int nBundles) {

	// parse inputs
	char * infile = filePath;

	GLfloat * positions = (GLfloat *) pyPositions;
	GLfloat * normals = (GLfloat *) pyNormals;
	GLint * colors = (GLint *) pyColors;

	GLuint * ebo = (GLuint *) pyEbo;
	int * fibersize = (int *) pyFiberSize;

	int * bundlestart = (int *) pyBundleStart;

	// open bundledata file
	FILE *fp;
	fp = fopen(infile, "rb");

	// read data
	unsigned k, index = 0, i, j;
	GLfloat normal[3] = {1.0, 1.0, 1.0};
	GLfloat norma = 1.0;

	for (i=1; i<nBundles; i++) {
		for (j=bundlestart[i-1]; j<bundlestart[i]; j++) {
			fread(&fibersize[j], sizeof(int), 1, fp);
			fread(positions, sizeof(GLfloat), fibersize[j]*3, fp);

			for (k=0; k<fibersize[j] - 1; k++) {
				*(ebo++) = index++;

				normal[0] = positions[k*3+3] - positions[ k*3 ];
				normal[1] = positions[k*3+4] - positions[k*3+1];
				normal[2] = positions[k*3+5] - positions[k*3+2];
				norma = sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2]);

				*(normals++) = normal[0]/norma;
				*(normals++) = normal[1]/norma;
				*(normals++) = normal[2]/norma;

				*(colors++) = (i-1);
			}

			*(ebo++) = index++;
			*(ebo++) = 0xFFFFFFFF;

			*(colors++) = (i-1);

			*(normals++) = normal[0]/norma;
			*(normals++) = normal[1]/norma;
			*(normals++) = normal[2]/norma;
			positions += fibersize[j]*3;
		}
	}

	fclose(fp);
}


void createVBOAndEBOFromPoints(void * pyPositions, 
    void * pyNormals, 
    void * pyColors, 
    void * pyEbo, 
    void * pyFiberSize, 
    void * pyBundleStart, 
    int curvesCount, 
    int nBundles) {

    // parse inputs
    GLfloat * positions = (GLfloat *) pyPositions;
    GLfloat * normals = (GLfloat *) pyNormals;
    GLint * colors = (GLint *) pyColors;

    GLuint * ebo = (GLuint *) pyEbo;
    int * fibersize = (int *) pyFiberSize;

    int * bundlestart = (int *) pyBundleStart;

    // read data
    unsigned k, index = 0, i, j;
    GLfloat normal[3] = {1.0, 1.0, 1.0};
    GLfloat norma = 1.0;

    for (i=1; i<nBundles; i++) {
        for (j=bundlestart[i-1]; j<bundlestart[i]; j++) {

            for (k=0; k<fibersize[j] - 1; k++) {
                *(ebo++) = index++;

                normal[0] = positions[k*3+3] - positions[ k*3 ];
                normal[1] = positions[k*3+4] - positions[k*3+1];
                normal[2] = positions[k*3+5] - positions[k*3+2];
                norma = sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2]);

                *(normals++) = normal[0]/norma;
                *(normals++) = normal[1]/norma;
                *(normals++) = normal[2]/norma;

                *(colors++) = (i-1);
            }

            *(ebo++) = index++;
            *(ebo++) = 0xFFFFFFFF;

            *(colors++) = (i-1);

            *(normals++) = normal[0]/norma;
            *(normals++) = normal[1]/norma;
            *(normals++) = normal[2]/norma;
            positions += fibersize[j]*3;
        }
    }
}

// In place segmentation function
int inPlaceSegmentationGenerateElementBuffer(int bundleN,
    int percentage,
    void *pyBundleStart,
    void *pyFiberSize,
    void *pySelectedBundles,
    void *pyEbo) {


    int *bundleStart = (int *) pyBundleStart;
    int *fiberSize = (int *) pyFiberSize;
    int *selectedBundles = (int *) pySelectedBundles;
    GLuint *ebo = (GLuint *) pyEbo;
    
    int eboSize = 0;
    int tmp = 0, index = 0, i, j, k;

    for (i=0; i<bundleN; i++) {
        if (selectedBundles[i])
            for (j=bundleStart[i]; j<bundleStart[i+1]; j++, tmp++) {
                if (tmp < percentage) {
                    eboSize += fiberSize[j] + 1;
                    for (k=0; k<fiberSize[j]; k++)
                        *(ebo++) = index++;
                    *(ebo++) = 0xFFFFFFFF;
                }
                else
                    index += fiberSize[j];

                if (tmp == 99)
                    tmp = -1;
            }

        else
            for (j=bundleStart[i]; j<bundleStart[i+1]; j++)
                index += fiberSize[j];
    }

    return eboSize; 
}


// In place segmentation export bundlesdata function
void inPlaceSegmentationExportbundlesdata(char * filePath,
    int bundleN,
    int percentage,
    void *pyBundleStart,
    void *pyFiberSize,
    void *pySelectedBundles,
    void *pyFiberCount,
    void *pyPoints) {


    int *bundleStart = (int *) pyBundleStart;
    int *fiberSize = (int *) pyFiberSize;
    int *selectedBundles = (int *) pySelectedBundles;
    int *fiberCount = (int *) pyFiberCount;
    GLfloat *points = (GLfloat *) pyPoints;

    // open bundledata file
    FILE *fp;
    fp = fopen(filePath, "wb");
    
    int tmp = 0, i, j, offset = 0;

    for (i=0; i<bundleN; i++) {
        if (selectedBundles[i])
            for (j=bundleStart[i], fiberCount[i]=offset; j<bundleStart[i+1]; j++, tmp++) {

                if (tmp < percentage) {
                    // fiberCount[i]++;
                    offset ++;
                    fwrite(fiberSize+j, sizeof(int), 1, fp);
                    fwrite(points, sizeof(GLfloat), fiberSize[j]*3, fp);
                }

                points += 3*fiberSize[j];

                if (tmp == 99)
                    tmp = -1;
            }

        else
            for (j=bundleStart[i]; j<bundleStart[i+1]; j++)
                points += 3*fiberSize[j];
    }
    fiberCount[i]=offset;

    fclose(fp);
}





/*

// Diego-Nicole's segmentation



void thresholdDialog::on_RunSegmentationButton_clicked()
{
    unsigned int ctr;
    unsigned int i,j,k;
    unsigned int lim;

    QElapsedTimer timer;



    //------------------------------------ Definicion de Subject ------------------------------------
    if (this->_bundle == NULL) {
        printf("ERROR! NO SE CARGO EL BUNDLE A SEGMENTAR!");
        exit(1);
    } else {
        this->nFibersS = this->_bundle->getCurves_Count();
    }

    //------------------------------------ Calculo de nuevos umbrales ------------------------------------

    //Se calculan los umbrales de cada bundle ACTIVO para los valores de min, max y step definidos
    for (i = 0; i < this->atlasTotalBundles; i++) {
        this->resetThresholdVector(i);
    }


    //-------------------- Reserva de memoria para Matriz de Resultados --------------------

    this->totalBunTHs = 0;

    for (i = 0; i < this->atlasTotalBundles; i++) {
        this->totalBunTHs += this->totalThreasholdsPerBundle[i];
    }

    free(this->Results);
    this->Results = NULL;

    this->Results = (char*)calloc(this->nFibersS * this->totalBunTHs, sizeof(char));
    if (this->Results == NULL) {
        printf("ERROR ALLOCATING MEMORY FOR RESULTS MATRIX [on_RunSegmentationButton_clicked()]");
    }


    //------------------------------------ Segmentacion Paralelizada ------------------------------------


    // Parceled processing. Depending of available memory we will process the dataset by using subsets of the entire dataset.
    lim = subjectSubset(this->nFibersS, this->nFibersA, this->totalBunTHs); // 50000

    timer.start();

    k = 0;    
    for (i = 0; i < this->atlasTotalBundles; i++) {

        for (j = 0; j < this->totalThreasholdsPerBundle[i]; j++) {

            if (this->_states[i] == true) {

                std::cout << "Bundle: " << i << "  Threshold: " << this->threasholdsPerBundle[i][j] << std::endl;

                // Segmentation function applied to subject per bundle and threshold
                this->segmentation((this->Results + k*this->nFibersS),                  //Result
                                   (this->nFibersS),                                    //nFibersS
                                   (this->atlasFibersPerBundle[i]),                     //nFibersA
                                   (this->Subject),                                     //Subject
                                   (this->Atlas + nData*this->fibersPerBundleUsed[i]),  //Atlas
                                   (this->threasholdsPerBundle[i][j]),                  //Threshold
                                   (lim));                                              //Lim

            }

            // barra de progreso de segmentacion
            ui->segmentationProgressBar->setValue(k*100/this->totalBunTHs);
            k += 1 ;

        }

    }

    std::cout << std::endl <<"tiempo total de segmentacion: " << timer.elapsed() << std::endl;
    timer.restart();


    this->dataSegmented = 1;

    // conteo de fibras segmentadas
    ctr=0;
    for (i=0; i<nFibersS*this->totalBunTHs; i++){
        if(Results[i] == 1)
            ++ctr;
    }
    std::cout << "\n\nFIBRAS FINALES: " << ctr << std::endl;

    // vector de posiciones para cada bundle en la matriz de resultados (usado en el shader)
    free(this->thresholdPos);
    this->thresholdPos = NULL;
    this->thresholdPos = (int*)malloc(this->atlasTotalBundles*sizeof(int));
    if (this->thresholdPos == NULL){std::cout << "ERROR: CANT MALLOC thresholdPos" << std::endl;}

    int sum = 0;
    this->thresholdPos[0] = 0;
    for (i = 1; i < this->atlasTotalBundles; i++) {
        sum += this->totalThreasholdsPerBundle[i-1];
        this->thresholdPos[i] = sum;
    }

    //------------------------------------ colors ------------------------------------

    float *colors = NULL;
    colors = (float*)calloc(3*this->nFibersS*this->totalBunTHs, sizeof(GL_FLOAT));
    if (colors == NULL) {std::cout << "ERROR ALLOCATING MEMORY FOR COLORS" << std::endl;}

    std::cout << "Total MBytes allocated for Colors: " << 3.0*this->nFibersS*this->totalBunTHs*sizeof(GL_FLOAT)/(1024*1024) << std::endl;

    timer.start();

    ctr = 0;

    for (i = 0; i < this->atlasTotalBundles; i++){

        for (j = 0; j < this->totalThreasholdsPerBundle[i]; j++) {

            for (k = 0; k < this->nFibersS; k++) {

                if (this->Results[ctr] == 1) {
                    colors[3*ctr+0] = this->bundleColors[3*i+0]/255.0;
                    colors[3*ctr+1] = this->bundleColors[3*i+1]/255.0;
                    colors[3*ctr+2] = this->bundleColors[3*i+2]/255.0;
                } else {
                    colors[3*ctr+0] = 0.0;
                    colors[3*ctr+1] = 0.0;
                    colors[3*ctr+2] = 0.0;
                }

                ctr += 1;

            }
        }
    }

    //std::cout << "tiempo total de color: " << timer.elapsed() << std::endl;
    timer.restart();

    //------------------------------------ OpenGL ------------------------------------


    // se activa el shader de bundles
    this->view->_bundle_shader->useProgram();

    // se bindea el VAO de bundles
    glBindVertexArray(this->view->_bundle_vao);

    // matriz de resultados a un texture buffer
    glGenBuffers(1, &this->view->tbo);
    glBindBuffer(GL_TEXTURE_BUFFER, this->view->tbo);
    glBufferData(GL_TEXTURE_BUFFER, 3*this->nFibersS*this->totalBunTHs*sizeof(GL_FLOAT), colors, GL_STATIC_DRAW);
    glGenTextures(1, &this->view->tex);
    glBindBuffer(GL_TEXTURE_BUFFER, 0);

    free(colors);

    // vector de colores hie
    glUniform1iv(this->view->_bundle_hieColors, 3*this->atlasTotalBundles, this->bundleColors);

    // vector de umbrales por bundle
    glUniform1iv(this->view->_bundle_thresholdPos, this->atlasTotalBundles, this->thresholdPos);

    // total de bundles
    glUniform1i(this->view->_bundle_bundlesTotal, this->atlasTotalBundles);

    // indice inicial bundle
    glUniform1i(this->view->_bundle_bundleIndex, this->_selectedBundle);

    // indice inicial umbral
    glUniform1i(this->view->_bundle_thresholdIndex, this->activeThresholdForBundle[this->_selectedBundle]);

    // Activa textura result
    glUniform1i(this->view->_bundle_segmentedByAtlas, 1);
    this->view->textureLoaded = 1;

    // total de fibras del sujeto
    glUniform1i(this->view->_bundle_fibersTotal, (int)this->nFibersS);

    // transparencia de fibras sin segmentar
    glUniform1f(this->view->_bundle_alpha, 99*1.0/100.0);

    // Se desbindea el VAO de bundle
    glBindVertexArray(0);

    // se renderiza
    this->view->updateGL();


    //------------------------------------ etc ------------------------------------

    // se reinicia la barra de progreso
    ui->segmentationProgressBar->setValue(0);
    ui->alphaSlider->setValue(99);

}











// Parallel segmentation of fibers (fast)
void thresholdDialog::segmentation(char *Results, unsigned nFibersS, unsigned int nFibersA, float *Subject, float *Atlas, float threshold, unsigned int lim)
{

    unsigned int it, num, nThreads;
    unsigned int  begin, end, nFibersSsub, nFibersSres;

    // Set the number of threads created.
    nThreads = omp_get_num_procs();
    //printf("Number of processors: %i\n", nThreads);

    // Parceled processing. Depending of available memory we will process the dataset by using subsets of the entire dataset.
    nFibersSsub = (nFibersS > lim) ? lim : nFibersS;

    num = nFibersS / nFibersSsub;
    nFibersSres = nFibersS % nFibersSsub;
    num = (nFibersSres != 0) ? (num + 1) : num;

    //printf("Iterations number: %i\n",num);
    //printf("Number of fibers per subset: %li\n",nFibersSsub);
    //printf("Number of fibers on last iteration: %li\n",nFibersSres);

    // Parallel configuration
    omp_set_num_threads(nThreads);

    //std::cout << "threshold: " << thresholds[i] << std::endl;

    // Iterations.
    for (it = 0; it < num; ++it) {

        begin = it*nFibersSsub;     // first fiber from this iterations subset
        end = (it + 1)*nFibersSsub; // last fiber from this iterations subset

        // last subset has just the remainder of the fibers
        if (nFibersSres != 0 && it == num-1) {
                    nFibersSsub = nFibersSres;
                    end = begin + nFibersSsub;
        }

        //printf("Iteration %i: beginning (%li) - ending(%li)\n",it, begin, end);

        #pragma omp parallel
        {

        //int ID = omp_get_thread_num();
        //printf ("Thread number: %i\n",ID);

        float subs, subsI, maximum, maximumI, sumS, sumA, fact, aux, Thr;
        unsigned int countNonDiscardedFibers1 = 0, countNonDiscardedFibers2 = 0,countNonDiscardedFibers4 = 0;
        unsigned int i, j, k, s, count, ctr;

        // Compute cuadratic threshold
        Thr = threshold*threshold;

        // Allocate memory for temporary results
        int totalBytes = 0;
        totalBytes += (nFibersSsub*nFibersA)/nThreads;
        totalBytes *= 2; // double the amount because we save both coordinates i,j.

        int *NotDiscarded = NULL;
        NotDiscarded = (int*)malloc(totalBytes*sizeof(int));
        if (NotDiscarded == NULL){fputs("Error allocating memory for temporary results\n", stderr); printf("\n%u\n", totalBytes); exit(1);}
        //else {printf("Temporary resuls memory successfully allocated (%p)\n", NotDiscarded);}

        //-------Process one central point----------

        #pragma omp for schedule(dynamic)
        for (j = begin; j < end; ++j) {

            for (i = 0; i < nFibersA; ++i) {

                subs = 0;
                subs += (Atlas[i*nData+10*DIM+0]-Subject[j*nData+10*DIM+0])*(Atlas[i*nData+10*DIM+0]-Subject[j*nData+10*DIM+0]);
                subs += (Atlas[i*nData+10*DIM+1]-Subject[j*nData+10*DIM+1])*(Atlas[i*nData+10*DIM+1]-Subject[j*nData+10*DIM+1]);
                subs += (Atlas[i*nData+10*DIM+2]-Subject[j*nData+10*DIM+2])*(Atlas[i*nData+10*DIM+2]-Subject[j*nData+10*DIM+2]);

                if(subs < Thr) {
                    NotDiscarded[countNonDiscardedFibers1*2 + 0] = j;
                    NotDiscarded[countNonDiscardedFibers1*2 + 1] = i;
                    countNonDiscardedFibers1 += 1;
                }

            }
        }


        //-------Process both extreme points----------

        //#pragma omp for schedule(dynamic)
        for (count=0; count<countNonDiscardedFibers1; count++) {

            j = NotDiscarded[count*2+0];
            i = NotDiscarded[count*2+1];

            maximum = 0;
            maximumI = 0;

            subs = 0;
            subs += (Atlas[i*nData+0]-Subject[j*nData+0])*(Atlas[i*nData+0]-Subject[j*nData+0]);
            subs += (Atlas[i*nData+1]-Subject[j*nData+1])*(Atlas[i*nData+1]-Subject[j*nData+1]);
            subs += (Atlas[i*nData+2]-Subject[j*nData+2])*(Atlas[i*nData+2]-Subject[j*nData+2]);

            subsI = 0;
            subsI += (Atlas[i*nData+(nPoints-1)*DIM+0]-Subject[j*nData+0])*(Atlas[i*nData+(nPoints-1)*DIM+0]-Subject[j*nData+0]);
            subsI += (Atlas[i*nData+(nPoints-1)*DIM+1]-Subject[j*nData+1])*(Atlas[i*nData+(nPoints-1)*DIM+1]-Subject[j*nData+1]);
            subsI += (Atlas[i*nData+(nPoints-1)*DIM+2]-Subject[j*nData+2])*(Atlas[i*nData+(nPoints-1)*DIM+2]-Subject[j*nData+2]);

            maximum = subs > maximum ? subs : maximum;
            maximumI = subsI > maximumI ? subsI : maximumI;

            subs = 0;
            subs += (Atlas[i*nData+20*DIM+0]-Subject[j*nData+20*DIM+0])*(Atlas[i*nData+20*DIM+0]-Subject[j*nData+20*DIM+0]);
            subs += (Atlas[i*nData+20*DIM+1]-Subject[j*nData+20*DIM+1])*(Atlas[i*nData+20*DIM+1]-Subject[j*nData+20*DIM+1]);
            subs += (Atlas[i*nData+20*DIM+2]-Subject[j*nData+20*DIM+2])*(Atlas[i*nData+20*DIM+2]-Subject[j*nData+20*DIM+2]);

            subsI = 0;
            subsI += (Atlas[i*nData+(nPoints-21)*DIM+0]-Subject[j*nData+20*DIM+0])*(Atlas[i*nData+(nPoints-21)*DIM+0]-Subject[j*nData+20*DIM+0]);
            subsI += (Atlas[i*nData+(nPoints-21)*DIM+1]-Subject[j*nData+20*DIM+1])*(Atlas[i*nData+(nPoints-21)*DIM+1]-Subject[j*nData+20*DIM+1]);
            subsI += (Atlas[i*nData+(nPoints-21)*DIM+2]-Subject[j*nData+20*DIM+2])*(Atlas[i*nData+(nPoints-21)*DIM+2]-Subject[j*nData+20*DIM+2]);

            maximum = subs > maximum ? subs : maximum;
            maximumI = subsI > maximumI ? subsI : maximumI;

            aux = maximum < maximumI ? maximum : maximumI;

            if(aux < Thr) {
                NotDiscarded[countNonDiscardedFibers2*2+0] = j;
                NotDiscarded[countNonDiscardedFibers2*2+1] = i;
                countNonDiscardedFibers2 += 1;
            }
        }


        //-------Process with 4 intermedial points-----------

        //#pragma omp for schedule(dynamic)
        for (count=0; count<countNonDiscardedFibers2; count++) {

            j = NotDiscarded[count*2+0];
            i = NotDiscarded[count*2+1];

            maximum = 0;
            maximumI = 0;

            char vec[4] = {3,7,13,17};

            for(s=0; s<4;++s) {

                char k = vec[s];
                subs = 0;
                subs += (Atlas[i*nData+k*DIM+0]-Subject[j*nData+k*DIM+0])*(Atlas[i*nData+k*DIM+0]-Subject[j*nData+k*DIM+0]);
                subs += (Atlas[i*nData+k*DIM+1]-Subject[j*nData+k*DIM+1])*(Atlas[i*nData+k*DIM+1]-Subject[j*nData+k*DIM+1]);
                subs += (Atlas[i*nData+k*DIM+2]-Subject[j*nData+k*DIM+2])*(Atlas[i*nData+k*DIM+2]-Subject[j*nData+k*DIM+2]);

                subsI = 0;
                subsI += (Atlas[i*nData+(nPoints-k-1)*DIM+0]-Subject[j*nData+k*DIM+0])*(Atlas[i*nData+(nPoints-k-1)*DIM+0]-Subject[j*nData+k*DIM+0]);
                subsI += (Atlas[i*nData+(nPoints-k-1)*DIM+1]-Subject[j*nData+k*DIM+1])*(Atlas[i*nData+(nPoints-k-1)*DIM+1]-Subject[j*nData+k*DIM+1]);
                subsI += (Atlas[i*nData+(nPoints-k-1)*DIM+2]-Subject[j*nData+k*DIM+2])*(Atlas[i*nData+(nPoints-k-1)*DIM+2]-Subject[j*nData+k*DIM+2]);

                maximum = subs > maximum ? subs : maximum;
                maximumI = subsI > maximumI ? subsI : maximumI;
            }

            aux = maximum < maximumI ? maximum : maximumI;

            if(aux < Thr) {
                NotDiscarded[countNonDiscardedFibers4*2+0] = j;
                NotDiscarded[countNonDiscardedFibers4*2+1] = i;
                countNonDiscardedFibers4 += 1;
            }

        }

        //-------Process with original algorithm and 21 points----------

        //#pragma omp for schedule(dynamic)
        for (count=0; count<countNonDiscardedFibers4; count++) {

            j = (NotDiscarded[count*2+0]);
            i = (NotDiscarded[count*2+1]);

            //Length factor (subject length)
            sumS = 0;
            sumS += ((Subject[j*nData+3]-Subject[j*nData+(0)])*(Subject[j*nData+3]-Subject[j*nData+(0)]));
            sumS += ((Subject[j*nData+4]-Subject[j*nData+(1)])*(Subject[j*nData+4]-Subject[j*nData+(1)]));
            sumS += ((Subject[j*nData+5]-Subject[j*nData+(2)])*(Subject[j*nData+5]-Subject[j*nData+(2)]));
            sumS = sqrt(sumS);

            //Length factor (atlas length)
            sumA = 0;
            sumA += ((Atlas[i*nData+3]-Atlas[i*nData+(0)])*(Atlas[i*nData+3]-Atlas[i*nData+(0)]));
            sumA += ((Atlas[i*nData+4]-Atlas[i*nData+(1)])*(Atlas[i*nData+4]-Atlas[i*nData+(1)]));
            sumA += ((Atlas[i*nData+5]-Atlas[i*nData+(2)])*(Atlas[i*nData+5]-Atlas[i*nData+(2)]));
            sumA = sqrt(sumA);

            fact = sumA < sumS ? ((sumS-sumA)/sumS) : ((sumA-sumS)/sumA);
            fact = (((fact + 1.0f)*(fact + 1.0f))-1.0f);
            fact = fact < 0.0f ? 0.0f : fact;

            // Euclidean distance
            maximum = 0;
            maximumI = 0;

            for (k = 0; k < nPoints; ++k) {

                subs  = 0;
                subsI = 0;

                for(s = 0; s < DIM; ++s) {
                    subs  += (Atlas[i*nData+(k*DIM+s)]-Subject[j*nData+(k*DIM+s)])*(Atlas[i*nData+(k*DIM+s)]-Subject[j*nData+(k*DIM+s)]);
                    subsI += (Atlas[i*nData+((nPoints-k-1)*DIM+s)]-Subject[j*nData+(k*DIM+s)])*(Atlas[i*nData+((nPoints-k-1)*DIM+s)]-Subject[j*nData+(k*DIM+s)]);
                }

                maximum = subs > maximum ? subs : maximum;
                maximumI = subsI > maximumI ? subsI : maximumI;
            }

            aux = (float)(sqrt(maximum < maximumI ? maximum : maximumI) + fact);

            if (aux < Thr)
                Results[j] = 1;

        }

        free(NotDiscarded);

        }

    }
}
*/