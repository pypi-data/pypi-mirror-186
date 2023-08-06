CPP=gcc

OBJECTS= ROISegmentationCFunctions.o #bundleCFunctions.o
BINS= bundleCFunctions
#CPPFLAGS=-Wall -g3 
#CPPFLAGS=-Wall -O9 -g -DNDEBUG
DEST=.

%.o: %.c
	$(CPP) $(CPPFLAGS) -c $< -o $@

all: bin

bin: $(OBJECTS) $(BINS)
	
bundleCFunctions:
	gcc $(CPPFLAGS) -o $(DEST)/bundleCFunctions bundleCFunctions.c $(OBJECTS) -lm -fopenmp 

clean:
	rm -f $(OBJECTS) $(BINS)
	cd $(DEST); rm -f *.a *.o *.c~ *.h~ $(BINS)
