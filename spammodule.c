#include <python.h>
#include <string.h>

static PyObject* spam_result(PyObject* self) {
	const char* str = "result: ";
	return Py_BuildValue("s", str);
}

static PyObject* spam_num(PyObject* self, PyObject* args) {
	int num;

	if (!PyArg_ParseTuple(args, "i", &num))
		return NULL;

	num = num - 1;
	return Py_BuildValue("i", num);
}

static PyMethodDef SpamMethods[] = {
	{"result", spam_result, METH_VARARGS, "print string"},
	{"num", spam_num, METH_VARARGS, "count data"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef spammodule = {
	PyModuleDef_HEAD_INIT,
	"spam",
	"It is a test module",
	-1, SpamMethods
};

PyMODINIT_FUNC PyInit_spam(void) {
	return PyModule_Create(&spammodule);
}