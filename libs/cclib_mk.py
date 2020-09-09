from pymakelib.Module import ModuleHandle

LIB_PATH = '/PROJECTS/C_C++/cclib/'


def getSrcs(m: ModuleHandle):
    try:
        srcs = [
            'cclib/cstring.c',
            'cclib/cstrfuncs.c',
            'cclib/cslice.c',
            'cclib/cprintf.c',
            'cclib/cmem.c',
            'cclib/cstrtok.c'
        ]
        return [LIB_PATH + s for s in srcs]
    except Exception as e:
        print(e)


def getIncs(m: ModuleHandle):
    return [LIB_PATH + 'cclib']