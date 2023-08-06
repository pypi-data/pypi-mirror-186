#include <Python.h>
#include <numpy/arrayobject.h>

PyObject * pyAlgo(PyObject* self, PyObject* args) {
	int a;

	if (!PyArg_ParseTuple(args,"i", &a))
		return NULL;

	return Py_BuildValue("i", a*a);
}