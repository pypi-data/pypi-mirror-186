from setuptools import setup, Extension
import numpy

module = Extension("FiberVis_core", sources = ["FiberVis_core.c", "bundleMethods.c", 
											"PointOctree.c",
											"AtlasBasedParallelSegmentation.c",
											# "ffclust.c",
											"test.c", "miscellaneous.c"])

setup(name="FiberVis_core",
		version = "1.0",
		description="This is a package test.",
		ext_modules=[module],
		include_dirs=[numpy.get_include()]
		)