#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "math.h"

#ifdef __APPLE__
#include <OpenGL/gl3.h>
#else
#include <GL/gl.h>
#endif

// struct trkHeader {
// 	char id_string[6];					// ID string for track file. The first 5 characters must be "TRACK".
// 	short int dim[3];					// Dimension of the image volume.
// 	float voxel_size[3];				// Voxel size of the image volume.
// 	float origin[3];					// Origin of the image volume. This field is not yet being used by TrackVis. That means the origin is always (0, 0, 0).
// 	short int n_scalars;				// Number of scalars saved at each track point (besides x, y and z coordinates).
// 	char scalar_name[10][20];			// Name of each scalar. Can not be longer than 20 characters each. Can only store up to 10 names.
// 	short int n_properties;				// Number of properties saved at each track.
// 	char property_name[10][20];			// Name of each property. Can not be longer than 20 characters each. Can only store up to 10 names.
// 	float vox_to_ras[4][4];				// 4x4 matrix for voxel to RAS (crs to xyz) transformation. If vox_to_ras[3][3] is 0, it means the matrix is not recorded. This field is added from version 2.
// 	char reserved[444];					// Reserved space for future version.
// 	char voxel_order[4];				// Storing order of the original image data. Explained here.
// 	char pad2[4];						// Paddings.
// 	float image_orientation_patient[6];	// Image orientation of the original image. As defined in the DICOM header.
// 	char pad1[2];						// Paddings.
// 	unsigned char invert_x;				// Inversion/rotation flags used to generate this track file. For internal use only.
// 	unsigned char invert_y;				// As above.
// 	unsigned char invert_z;				// As above.
// 	unsigned char swap_xy;				// As above.
// 	unsigned char swap_yz;				// As above.
// 	unsigned char swap_zx;				// As above.
// 	int n_count;						// Number of tracks stored in this track file. 0 means the number was NOT stored.
// 	int version;						// Version number. Current version is 2.
// 	int hdr_size;						// Size of the header. Used to determine byte swap. Should be 1000.
// }; 										// 1000 bits total
// typedef struct trkHeader trkHeader;

// int readTrkHeader(char * filePath, short int * nScalars, short int * nProperties, int * nCount, unsigned long * fileSize, int * headerSize) {
// 	/// based in http://www.trackvis.org/docs/?subsect=fileformat
// 	FILE *fp;
// 	fp = fopen(filePath, "rb");

// 	trkHeader headerBuffer;
// 	fread(&headerBuffer, 1, sizeof(trkHeader), fp);

// 	fseek(fp, 0L, SEEK_END);
// 	*fileSize = ftell(fp);
// 	fclose(fp);

// 	// copie the important data
// 	*nScalars = headerBuffer.n_scalars;
// 	*nProperties = headerBuffer.n_properties;
// 	*nCount = headerBuffer.n_count;
// 	*headerSize = headerBuffer.hdr_size;

// 	*fileSize = *fileSize - headerBuffer.hdr_size;

// 	// Check that the file corresponds with a fiber file
// 	if (strcmp(headerBuffer.id_string, "TRACK") != 0) return -1;
// 	if (headerBuffer.hdr_size != 1000) return -1;
// 	return 0;
// }

// int readTrkBody(char * filePath, 
// 	int headerSize, 
// 	short int nScalars,
// 	short int nProperties,
// 	void * pyPoints, 
// 	void * pyNormals, 
// 	void * pyEbo, 
// 	void * pyFiberSize, 
// 	int curvesCount, 
// 	void * pyScalars,
// 	void * pyProperties) {

// 	// parse inputs
// 	GLfloat * points = (GLfloat *) pyPoints;
// 	GLfloat * normals = (GLfloat *) pyNormals;

// 	GLuint * ebo = (GLuint *) pyEbo;
// 	int * fibersize = (int *) pyFiberSize;

// 	float * scalars = (float *) pyScalars;
// 	float * properties = (float *) pyProperties;

// 	int i, j, pointPack = 3+nScalars;

// 	// open bundledata file
// 	FILE *fp;
// 	fp = fopen(filePath, "rb");
// 	fseek(fp, headerSize, SEEK_SET);

// 	//////////////////////////////////////////////////////////////////////////////
// 	void readPoints() {
// 		fread(points, sizeof(GLfloat), fibersize[i]*3, fp);
// 	}

// 	void readPointsScalars() {
// 		for(j=0; j<fibersize[i]; j++) {
// 			fread(points+j*pointPack, sizeof(GLfloat), 3, fp);
// 			fread(scalars+j*nScalars, sizeof(float), nScalars, fp);
// 		}
// 		scalars += fibersize[i]*nScalars;
// 	}

// 	void readPointsProperties() {
// 		fread(points, sizeof(GLfloat), fibersize[i]*3, fp);
// 		fread(properties, sizeof(float), nProperties, fp);
// 		properties += nProperties;
// 	}

// 	void readPointsScalarsProperties() {
// 		for(j=0; j<fibersize[i]; j++) {
// 			fread(points+j*pointPack, sizeof(GLfloat), 3, fp);
// 			fread(scalars+j*nScalars, sizeof(float), nScalars, fp);
// 		}
// 		fread(properties, sizeof(float), nProperties, fp);

// 		scalars += fibersize[i]*nScalars;
// 		properties += nProperties;
// 	}

// 	void (*readData_i) ();

// 	if (nScalars == 0 && nProperties == 0) readData_i = readPoints;
// 	else if (nScalars != 0 && nProperties == 0) readData_i = readPointsScalars;
// 	else if (nScalars == 0 && nProperties != 0) readData_i = readPointsProperties;
// 	else readData_i = readPointsScalarsProperties;
// 	//////////////////////////////////////////////////////////////////////////////

// 	unsigned k, index = 0;
// 	GLfloat normal[3] = {1.0, 1.0, 1.0};
// 	GLfloat norma = 1.0;

// 	for (i=0; i<curvesCount; i++) {
// 		fread(&fibersize[i], sizeof(int), 1, fp);
// 		readData_i();

// 		for (k=0; k<fibersize[i] - 1; k++) {
// 			*(ebo++) = index++;

// 			normal[0] = points[k*3+3] - points[ k*3 ];
// 			normal[1] = points[k*3+4] - points[k*3+1];
// 			normal[2] = points[k*3+5] - points[k*3+2];
// 			norma = sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2]);

// 			*(normals++) = normal[0]/norma;
// 			*(normals++) = normal[1]/norma;
// 			*(normals++) = normal[2]/norma;
// 		}

// 		*(ebo++) = index++;
// 		*(ebo++) = 0xFFFFFFFF;

// 		*(normals++) = normal[0]/norma;
// 		*(normals++) = normal[1]/norma;
// 		*(normals++) = normal[2]/norma;
// 		points += fibersize[i]*3;
// 	}
	
// 	return 0;
// }

void readTckHeader(char * filePath, int * nCount, unsigned long * fileSize, int * headerSize) {
	FILE *fp;
	fp = fopen(filePath, "rb");

	// tmp the fixed size n
	int n = 1000;
	char headerSizeFound = 0, countFound = 0;
	char * headerBuffer = (char*) malloc(n*sizeof(char));

	do {
		fread(headerBuffer, n, sizeof(char), fp);

		if (strstr(headerBuffer, "file:") != NULL) {
			sscanf(strstr(headerBuffer, "file:"), "file: . %d", headerSize);
			headerSizeFound = 1;
		}

		if (strstr(headerBuffer, "count:") != NULL) {
			sscanf(strstr(headerBuffer, "count:"), "count: %d", nCount);
			countFound = 1;
		}

	} while (strstr(headerBuffer, "END") == NULL);


	fseek(fp, 0L, SEEK_END);
	*fileSize = ftell(fp);
	fclose(fp);

	*fileSize = *fileSize - *headerSize;
	printf("%lu\n", *fileSize);

	// printf("%s\n", headerBuffer);
}

int readTckBody(char * filePath, 
	int headerSize, 
	void * pyPoints, 
	void * pyNormals, 
	void * pyEbo, 
	void * pyFiberSize, 
	int curvesCount) {

	// parse inputs
	GLfloat * points = (GLfloat *) pyPoints;
	GLfloat * normals = (GLfloat *) pyNormals;

	GLuint * ebo = (GLuint *) pyEbo;
	int * fibersize = (int *) pyFiberSize;

	// open bundledata file
	FILE *fp;
	fp = fopen(filePath, "rb");
	fseek(fp, headerSize, SEEK_SET);

	unsigned k, index = 0;
	GLfloat normal[3] = {1.0, 1.0, 1.0};
	GLfloat norma = 1.0;

	float tmpVertex[3];

	fpos_t position;
	for (unsigned i=0; i<curvesCount; i++) {
		for(fread(tmpVertex, 3, sizeof(float), fp); *tmpVertex != 0x7fc00000 /*&& tmpVertex[0] !=*/; fread(tmpVertex, 3, sizeof(float), fp)) {
			memcpy(points+fibersize[i]*3, tmpVertex, sizeof(float)*3);

			fibersize[i]++;
		}
		printf("%u\n", i);

		for (unsigned k=0; k<fibersize[i] - 1; k++) {
			*(ebo++) = index++;

			normal[0] = points[k*3+3] - points[ k*3 ];
			normal[1] = points[k*3+4] - points[k*3+1];
			normal[2] = points[k*3+5] - points[k*3+2];
			norma = sqrt(normal[0]*normal[0] + normal[1]*normal[1] + normal[2]*normal[2]);

			*(normals++) = normal[0]/norma;
			*(normals++) = normal[1]/norma;
			*(normals++) = normal[2]/norma;
		}

		*(ebo++) = index++;
		*(ebo++) = 0xFFFFFFFF;

		*(normals++) = normal[0]/norma;
		*(normals++) = normal[1]/norma;
		*(normals++) = normal[2]/norma;
		points += fibersize[i]*3;
	}

	points = (GLfloat *) pyPoints;
	
	return 0;
}

int main(void) {
	// Trk
	// char * infile = "D:/Codes/UDEC/Database/trk/whole_brain.trk";
	// char * infile = "D:/Codes/UDEC/Database/forPamela_deMaximeDescoteaux/surgery_2018-12-17/results/raw/PFT_Tracking/raw__tracking.trk";

	// short int nProperties, nScalars;
	// int nCount, headerSize;
	// unsigned long fileSize;

	// printf("%u\n", readTrkHeader(infile, &nScalars, &nProperties, &nCount, &fileSize, &headerSize));

	// unsigned long intsOrFloats = (fileSize/4-nCount*(nProperties+1))*3/(3+nScalars);

	// void * points = malloc(intsOrFloats*4);
	// void * normals = malloc(intsOrFloats*4);
	// void * ebo = malloc((intsOrFloats/3+nCount)*4);
	// void * fibersize = malloc(nCount*4);

	// readTrkBody(infile, headerSize, nScalars, nProperties, points, normals, ebo, fibersize, nCount, NULL, NULL);

	// float * dots = (float*) points;

	// printf("[%.6f %.6f %.6f]\n", dots[0], dots[1], dots[2]);

	/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	// Tck
	char * infile = "D:/Codes/UDEC/Database/HCP1200-3M/101006/IN/3Msift.tck";

	int count, hdrSize;
	unsigned long fileSize;

	readTckHeader(infile, &count, &fileSize, &hdrSize);

	printf("file: %s\nncount: %d\nfileSize: %ld\nheaderSize: %d\n", infile, count, fileSize, hdrSize);

	void * points = malloc(fileSize-12-12*count);
	void * normals = malloc(fileSize-12-12*count);
	void * ebo = malloc((fileSize-12-12*count)/3+count*4);
	void * fiberSize = malloc(count*sizeof(int));
	memset(fiberSize, 0, count*sizeof(int));

	readTckBody(infile, hdrSize, points, normals, ebo, fiberSize, count);

	fileSize = (fileSize-12-12*count)/4;
	printf("%lu\n", fileSize);

	// GLuint * ebo2 = (GLuint *) ebo;
	// for (int i=((fileSize-12-12*count)/3+count*4)/4-5; i<((fileSize-12-12*count)/3+count*4)/4; i++)
	// 	printf("ebo: %u\n", ebo2[i]);

	return 0;
}

//4601133427556145136
//2041108464
//2041108464
//501277113
//501277113

/*



original:
whole_brain: [37.619522 45.870037 16.494087]						0.0988 sec
surgery_2018-12-17: [-24.227562   44.149063   -4.3723907]			29.3946 sec
surgery_2019-01-10: [-37.45662   50.222183   8.019493]				34.9868 sec


new:
whole_brain: [37.619522 45.870037 16.494087]						0.0101 sec
surgery_2018-12-17: [-24.227562   44.149063   -4.3723907]			1.2359 sec
surgery_2019-01-10: [-37.45661   50.222183   8.01949 ]				1.4556 sec


whole_brain:
HEADER









bool Fibers::loadMRtrix( const wxString &filename )
{
	Logger::getInstance()->print( wxT( "Loading MRtrix file" ), LOGLEVEL_MESSAGE );
	wxFile dataFile;
	long int nSize = 0;
	long int pc = 0, nodes = 0;
	converterByteFloat cbf;
	float x, y, z, x2, y2, z2;
	std::vector< float > tmpPoints;
	vector< vector< float > > lines;

	//Open file
	FILE *pFs = fopen( filename.ToAscii(), "r" ) ;
	////
	// read header
	////
	char lineBuffer[200];
	std::string readLine("");
	bool countFieldFound( false );

	while(readLine.find( "END" ) == std::string::npos)
	{
		fgets( lineBuffer, 200, pFs );

		readLine = std::string( lineBuffer );

		if( readLine.find( "file" ) != std::string::npos )
		{
			sscanf( lineBuffer, "file: . %ld", &pc );
		}

		if( readLine.find( "count" ) != std::string::npos && !countFieldFound )
		{
			sscanf( lineBuffer, "count: %d", &m_countLines );
			countFieldFound = true;
		}
	}

	fclose( pFs );

	if( dataFile.Open( filename ) )
	{
		nSize = dataFile.Length();

		if( nSize < 1 )
		{
			return false;
		}
	}

	nSize -= pc;
	dataFile.Seek( pc );
	wxUint8 *pBuffer = new wxUint8[nSize];
	dataFile.Read( pBuffer, nSize );
	dataFile.Close();

	Logger::getInstance()->print( wxT( "Reading fibers" ), LOGLEVEL_DEBUG );
	pc = 0;
	m_countPoints = 0; // number of points

	for( int i = 0; i < m_countLines; i++ )
	{
		tmpPoints.clear();
		nodes = 0;
		// read one tract
		cbf.b[0] = pBuffer[pc++];
		cbf.b[1] = pBuffer[pc++];
		cbf.b[2] = pBuffer[pc++];
		cbf.b[3] = pBuffer[pc++];
		x = cbf.f;
		cbf.b[0] = pBuffer[pc++];
		cbf.b[1] = pBuffer[pc++];
		cbf.b[2] = pBuffer[pc++];
		cbf.b[3] = pBuffer[pc++];
		y = cbf.f;
		cbf.b[0] = pBuffer[pc++];
		cbf.b[1] = pBuffer[pc++];
		cbf.b[2] = pBuffer[pc++];
		cbf.b[3] = pBuffer[pc++];
		z = cbf.f;
		//add first point
		tmpPoints.push_back( x );
		tmpPoints.push_back( y );
		tmpPoints.push_back( z );
		++nodes;
		x2 = x;
		cbf.f = x2;

		//Read points (x,y,z) until x2 equals NaN (0x0000C07F), meaning end of the tract.
		while( !( cbf.b[0] == 0x00 && cbf.b[1] == 0x00 && cbf.b[2] == 0xC0 && cbf.b[3] == 0x7F ) )
		{
			cbf.b[0] = pBuffer[pc++];   // get next float
			cbf.b[1] = pBuffer[pc++];
			cbf.b[2] = pBuffer[pc++];
			cbf.b[3] = pBuffer[pc++];
			x2 = cbf.f;
			cbf.b[0] = pBuffer[pc++];
			cbf.b[1] = pBuffer[pc++];
			cbf.b[2] = pBuffer[pc++];
			cbf.b[3] = pBuffer[pc++];
			y2 = cbf.f;
			cbf.b[0] = pBuffer[pc++];
			cbf.b[1] = pBuffer[pc++];
			cbf.b[2] = pBuffer[pc++];
			cbf.b[3] = pBuffer[pc++];
			z2 = cbf.f;

			// downsample fibers: take only points in distance of min 0.75 mm
			if( ( ( x - x2 ) * ( x - x2 ) + ( y - y2 ) * ( y - y2 ) + ( z - z2 ) * ( z - z2 ) ) >= 0.2 )
			{
				x = x2;
				y = y2;
				z = z2;
				tmpPoints.push_back( x );
				tmpPoints.push_back( y );
				tmpPoints.push_back( z );
				++nodes;
			}

			cbf.f = x2;
		}

		// put the tract in the line array
		lines.push_back( tmpPoints );

		for( int i = 0; i < nodes ; i++ )
		{
			m_countPoints++;
		}
	}

	delete[] pBuffer;
	pBuffer = NULL;

	////
	//POST PROCESS: set all the data in the right format for the navigator
	////
	m_pointArray.max_size();
	m_linePointers.resize( m_countLines + 1 );
	m_pointArray.resize( m_countPoints * 3 );
	m_linePointers[m_countLines] = m_countPoints;
	m_reverse.resize( m_countPoints );
	m_selected.resize( m_countLines, false );
	m_filtered.resize( m_countLines, false );
	m_linePointers[0] = 0;

	for( int i = 0; i < m_countLines; ++i )
	{
		m_linePointers[i + 1] = m_linePointers[i] + lines[i].size() / 3;
	}

	int lineCounter = 0;

	for( int i = 0; i < m_countPoints; ++i )
	{
		if( i == m_linePointers[lineCounter + 1] )
		{
			++lineCounter;
		}

		m_reverse[i] = lineCounter;
	}

	unsigned int pos = 0;
	vector< vector< float > >::iterator it;

	for( it = lines.begin(); it < lines.end(); it++ )
	{
		vector< float >::iterator it2;

		for( it2 = ( *it ).begin(); it2 < ( *it ).end(); it2++ )
		{
			m_pointArray[pos++] = *it2;
		}
	}

	// The MrTrix fibers are defined in the same geometric reference
	// as the anatomical file. That is, the fibers coordinates are related to
	// the anatomy in world space. The transformation from local to world space
	// for the anatomy is encoded in the m_dh->m_niftiTransform member.
	// Since we do not consider this tranform when loading the anatomy, we must
	// bring back the fibers in the same reference, using the inverse of the
	// local to world transformation. A further problem arises when loading an
	// anatomy that has voxels with dimensions differing from 1x1x1. The
	// scaling factor is encoded in the transformation matrix, but we do not,
	// for the moment, use this scaling. Therefore, we must remove it from the
	// the transformation matrix before computing its inverse.
	FMatrix localToWorld = FMatrix( DatasetManager::getInstance()->getNiftiTransform() );

	float voxelX = DatasetManager::getInstance()->getVoxelX();
	float voxelY = DatasetManager::getInstance()->getVoxelY();
	float voxelZ = DatasetManager::getInstance()->getVoxelZ();

	if( voxelX != 1.0 || voxelY != 1.0 || voxelZ != 1.0 )
	{
		FMatrix rotMat( 3, 3 );
		localToWorld.getSubMatrix( rotMat, 0, 0 );

		FMatrix scaleInversion( 3, 3 );
		scaleInversion( 0, 0 ) = 1.0 / voxelX;
		scaleInversion( 1, 1 ) = 1.0 / voxelY;
		scaleInversion( 2, 2 ) = 1.0 / voxelZ;

		rotMat = scaleInversion * rotMat;

		localToWorld.setSubMatrix( 0, 0, rotMat );
	}

	FMatrix invertedTransform( 4, 4 );
	invertedTransform = invert( localToWorld );

	for( int i = 0; i < m_countPoints * 3; ++i )
	{
		FMatrix curPoint( 4, 1 );
		curPoint( 0, 0 ) = m_pointArray[i];
		curPoint( 1, 0 ) = m_pointArray[i + 1];
		curPoint( 2, 0 ) = m_pointArray[i + 2];
		curPoint( 3, 0 ) = 1;

		FMatrix invertedPoint = invertedTransform * curPoint;

		m_pointArray[i] = invertedPoint( 0, 0 );
		m_pointArray[i + 1] = invertedPoint( 1, 0 );
		m_pointArray[i + 2] = invertedPoint( 2, 0 );

		i += 2;
	}

	Logger::getInstance()->print( wxT( "TCK file loaded" ), LOGLEVEL_MESSAGE );
	createColorArray( false );
	m_type = FIBERS;
	m_fullPath = filename;

#ifdef __WXMSW__
	m_name = wxT( "-" ) + filename.AfterLast( '\\' );
#else
	m_name = wxT( "-" ) + filename.AfterLast( '/' );
#endif
	return true;
}
/*
*/