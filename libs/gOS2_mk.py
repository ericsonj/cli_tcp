from pymakelib.Module import ModuleHandle

LIB_PATH = '/PROJECTS/C_C++/gOS2/'

def getSrcs(m: ModuleHandle):
    srcs = [
        'gOS2/audio.c',
        'gOS2/g_audiosrc.c',
        'gOS2/g_cmsis_os.c',
        'gOS2/g_freertos.c',
        'gOS2/g_multimedia_appsink.c',
        'gOS2/g_multimedia.c',
        'gOS2/g_ip_addr.c',
        'gOS2/dns.c',
    ]
    return [LIB_PATH + s for s in srcs]



def getIncs(m: ModuleHandle):
    return [LIB_PATH + 'gOS2', 'libs']