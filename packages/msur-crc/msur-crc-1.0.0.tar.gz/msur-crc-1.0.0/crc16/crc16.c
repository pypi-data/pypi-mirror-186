#include <Python.h>
#ifdef __cplusplus
#include <cstdint>
static const unsigned int CRC16 = 0x8005;
#else
#include<stdint.h>
#include <stddef.h>
#define CRC16 0x8005
#endif


uint16_t crc16(const uint8_t *data, uint16_t size) {
    uint16_t out = 0;
    int bits_read = 0;
    int bit_flag;

    if (data == NULL) {
        return 0;
    }

    while (size > 0) {
        bit_flag = out  >> 15;
        out <<= 1;
        out |= (*data >> (7 - bits_read)) & 1;
        bits_read++;
        if (bits_read > 7) {
            bits_read = 0;
            data ++;
            size --;
        }
        if (bit_flag) {
            out ^= CRC16;
        }
    }
    return out;
}


static PyObject* crc16_py(PyObject* self, PyObject* args) {
    PyObject *result = NULL;
    PyObject* package;

    if (PyArg_ParseTuple(args, "S", &package)) {
        char* data;
        Py_ssize_t size;
        PyBytes_AsStringAndSize(package, &data, &size);
        result = Py_BuildValue("L", crc16((uint8_t*)data, (uint16_t)size));
    }
    return result;
}

static char crc16_docs[] = "crc16(bytes): возвращает посчитанную контрольную сумму для строки байтов\n";

static PyMethodDef crc16_module_methods[] = {
    {"crc16", (PyCFunction)crc16_py,
     METH_VARARGS, crc16_docs},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef crc16_module_definition = {
    PyModuleDef_HEAD_INIT,
    "crc16",
    "Расширение предоставляет функцию вычисления контрольной суммы",
    -1,
    crc16_module_methods
};

PyMODINIT_FUNC PyInit_crc16(void) {
    return PyModule_Create(&crc16_module_definition);
}
