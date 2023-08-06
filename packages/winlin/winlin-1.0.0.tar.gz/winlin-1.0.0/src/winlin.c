#include <Python.h>
#include <xdo.h>


static PyObject* resize(PyObject* self, PyObject *args){
    int wid, w, h;
    if (!PyArg_ParseTuple(args, "iii", &wid, &w, &h))
        return NULL;

    xdo_t *xdo_inst = xdo_new(NULL);
    xdo_set_window_size(xdo_inst, wid, w, h, 0);
    xdo_free(xdo_inst);
    Py_RETURN_NONE;
    //return Py_BuildValue("s", "it worked, maybe?");
}
static char resize_docs[] = "\
change the size of a given window given its id and a new height and width\n\
";
/*----------------------------------------------------------------------------*/

static PyObject* move(PyObject* self, PyObject *args){
    int wid, x, y;
    if (!PyArg_ParseTuple(args, "iii", &wid, &x, &y))
        return NULL;

    xdo_t *xdo_inst = xdo_new(NULL);
    xdo_move_window(xdo_inst, wid, x, y);
    xdo_free(xdo_inst);
    Py_RETURN_NONE;
}
static char move_docs[] = "\
change the position of a window given its id and a new x and y\n\
";

/*----------------------------------------------------------------------------------*/
static PyMethodDef winlin_funcs[] = {
    {"resize", (PyCFunction)resize, METH_VARARGS, resize_docs},
    {"move", (PyCFunction)move, METH_VARARGS, move_docs},
    {NULL}
};

static char winlin_module_docs[] = "Module used to manipulate windows in linux";

static struct PyModuleDef winlin_module = {
	PyModuleDef_HEAD_INIT,
	"winlin",
	winlin_module_docs,
	-1,
	winlin_funcs
};

PyMODINIT_FUNC
PyInit_winlin(void){
    PyObject* m = PyModule_Create(&winlin_module);
    return m;
}
