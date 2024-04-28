#ifndef PYTHON_H
#define PYTHON_H

typedef int PyObject;
typedef int Py_ssize_t;
typedef int Py_UNICODE;

#define PyUnicode_Check(p) 1
#define PyUnicode_GET_LENGTH(p) 10
#define PyUnicode_AsUnicode(p) L"example_string"
#define PyUnicode_AsUTF8(p) "example_string"
#define PyUnicode_IS_COMPACT_ASCII(p) 1
#define PyUnicode_IS_COMPACT(p) 1

#endif /* PYTHON_H */
