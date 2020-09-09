from pymakelib.Module import ModuleHandle

HTTP_PATH = '/PROJECTS/C_C++/netlib/HTTP'
RRUTIL_PATH = '/PROJECTS/C_C++/netlib/RRUtil'
TCP_SERVER_PATH = '/PROJECTS/C_C++/netlib/TCPLib'
CLOG_PATH = '/PROJECTS/C_C++/netlib/clog'

def getSrcs(m: ModuleHandle):
    http_srcs = [
        'HTTP.c',
        'HTTPServer.c',
        'HTTPUtil.c',
        'apps/HTTPServer_index.c',
        'apps/HTTPServer_upload.c']
    
    rrutil_srcs = [
        'RRUtil.c'
        ]
    
    tcp_srcs = [
        'TCPServer.c',
        'TCPClient.c'
        ]
    
    clog = [
        'clog.c'
        ]
    
    srsc =  [ HTTP_PATH + '/' + s for s in http_srcs]
    srsc += [ RRUTIL_PATH + '/' + s for s in rrutil_srcs]
    srsc += [ TCP_SERVER_PATH + '/' + s for s in tcp_srcs]
    srsc += [ CLOG_PATH + '/' + s for s in clog]
    return srsc


def getIncs(m: ModuleHandle):
    return [HTTP_PATH + '/Include', RRUTIL_PATH, TCP_SERVER_PATH, CLOG_PATH]


