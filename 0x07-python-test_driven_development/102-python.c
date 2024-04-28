#include <Python.h>

void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    Py_UNICODE *unicode_str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    unicode_str = PyUnicode_AsUnicode(p);

    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        printf("  type: compact ascii\n");
        printf("  length: %ld\n", length);
        printf("  value: %s\n", PyUnicode_AsUTF8(p));
    }
    else if (PyUnicode_IS_COMPACT(p))
    {
        printf("  type: compact unicode object\n");
        printf("  length: %ld\n", length);
        printf("  value: %ls\n", unicode_str);
    }
    else
    {
        printf("  type: Unicode object\n");
        printf("  length: %ld\n", length);
        printf("  value: %ls\n", unicode_str);
    }
}
