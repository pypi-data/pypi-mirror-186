/*========================================================================================
strcompare_module.c
Pythod module definition for strcompare.
Version 1.2.1

Included functions
------------------
cdist_score.h
    cdist_score

fss_score.h
    fss_score
    adjusted_fss_score
    naive_fss_score
    adjusted_naive_fss_score

lcs_score.h
    lcs_score
    naive_lcs_score

levenshtein_score.h
    levenshtein_score
========================================================================================*/
#include <Python.h>

#include "compare_functions/cdist_score.h"
#include "compare_functions/fss_score.h"
#include "compare_functions/lcs_score.h"
#include "compare_functions/levenshtein_score.h"


/*========================================================================================
Wrap C functions into python object returning functions
========================================================================================*/

static PyObject* method_cdist_score(PyObject* self, PyObject *args)
{
    char *str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;
    
    score = cdist_score(str1, str2);
    return PyFloat_FromDouble(score);
}

static PyObject* method_fss_score(PyObject* self, PyObject *args)
{
    char *str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;

    score = fss_score(str1, str2);
    return PyFloat_FromDouble(score);
}

static PyObject* method_adjusted_fss_score(PyObject* self, PyObject *args)
{
    char *str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;

    score = adjusted_fss_score(str1, str2);
    return PyFloat_FromDouble(score);
}

static PyObject* method_naive_fss_score(PyObject* self, PyObject *args)
{
    char *str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;

    score = naive_fss_score(str1, str2);
    return PyFloat_FromDouble(score);
}

static PyObject* method_adjusted_naive_fss_score(PyObject* self, PyObject *args)
{
    char *str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;

    score = adjusted_naive_fss_score(str1, str2);
    return PyFloat_FromDouble(score);
}

static PyObject* method_lcs_score(PyObject* self, PyObject *args)
{
    char *str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;

    score = lcs_score(str1, str2);
    return PyFloat_FromDouble(score);
}

static PyObject* method_naive_lcs_score(PyObject* self, PyObject *args)
{
    char *str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;

    score = naive_lcs_score(str1, str2);
    return PyFloat_FromDouble(score);
}

static PyObject* method_levenshtein_score(PyObject* self, PyObject *args)
{
    char* str1, *str2;
    double score;

    if (!PyArg_ParseTuple(args, "ss", &str1, &str2))
        return NULL;

    score = levenshtein_score(str1, str2);
    return PyFloat_FromDouble(score);
}


/*========================================================================================
Define python functions
========================================================================================*/

static PyMethodDef strcompare_methods[] = {
    {
        "cdist_score", method_cdist_score, METH_VARARGS,
        "Character Distribution Score. Compares the character distribution between two "
        "strings.",
    },
    {
        "fss_score", method_fss_score, METH_VARARGS,
        "Fractured Substring Score. Identifies sequences of characters with the same "
        "relative order bewteen two strings"
    },
    {
        "adjusted_fss_score", method_adjusted_fss_score, METH_VARARGS,
        "Adjusted Fractured Substring Score. Identifies sequences of characters with the "
        "same relative order between two strings, adjusted for differences in distances "
        "between two matching characters in the first and second."
    },
    {
        "naive_fss_score", method_naive_fss_score, METH_VARARGS,
        "Naive Fractured Substring Score. Employes a naive algorithm to identify "
        "sequences of characters with the same relative order between two strings."
    },
    {
        "adjusted_naive_fss_score", method_adjusted_naive_fss_score, METH_VARARGS,
        "Naive Adjusted Fractured Substring Score. Employes a naive algorithm to "
        "identify sequences of characters with the same relative order between two "
        "strings, while also correcting for differences in index offsets between those "
        "characters in the first and second strings."
    },
    {
        "lcs_score", method_lcs_score, METH_VARARGS,
        "Longest Common Substring Score. Assesses similarity between two strings by "
        "identifying the longest substring common to both strings."
    },
    {
        "naive_lcs_score", method_naive_lcs_score, METH_VARARGS,
        "Naive Longest Common Substring Score. Employs a naive algorithm to "
        "assess the similarity of two strings by identifying the longest substring "
        "common to both strings."
    },
    {
        "levenshtein_score", method_levenshtein_score, METH_VARARGS,
        "Levenshtein Score. Assesses the similarity between two strings by calculating "
        "the levenshtein distance between the two and returning the proportion of the "
        "difference between the maximum possible distance and the calculated distance " 
        "to the maximum possible distance."
    },
    {NULL, NULL, 0, NULL}
};


/*========================================================================================
Define python module struct
========================================================================================*/

static struct PyModuleDef strcompare_module = {
    PyModuleDef_HEAD_INIT,
    "strcompare",
    "Methods to assess string similarity",
    -1,
    strcompare_methods
};


/*========================================================================================
Define module initialization function
========================================================================================*/


PyMODINIT_FUNC PyInit_strcompare(void)
{
    return PyModule_Create(&strcompare_module);
}
