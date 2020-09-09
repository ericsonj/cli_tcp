#include <stdint.h>
#include <stdlib.h>
#include <unistd.h>
#include "RRUtil.h"
#include "cmacros.h"
#include "cstring.h"
#include "cmsis_os2.h"
#include "TCPServer.h"
#include "example_misc.h"
#include "microrl.h"
#include "ring_buffer.h"

Connection        conn;
SemaphoreHandle_t sem;
char              inputchar;

RINGBUFF_T rbuff;
uint8_t    inputBuff[512];

//*****************************************************************************
// print callback for microrl library
void print(const char* str) {
	fprintf (stdout, "%s", str);
    TCPServer_write(&conn, (uint8_t*)str, strlen(str));
}

//*****************************************************************************
// get char user pressed, no waiting Enter input
char get_char(void) {
    char c = 0;
    while (RingBuffer_Pop(&rbuff, &c) == 0) {
        osDelay(50);
    }
    return c;
}

static AppState term_recv(Connection* conn, uint8_t* data, uint32_t nbrOfBytes) {
    for (int i = 0; i < nbrOfBytes; ++i) {
        printf("%c\n", (char)data[i]);
    }
    RingBuffer_InsertMult(&rbuff, data, nbrOfBytes);
    return appOK;
}

static void term_close(uint8_t connIdx) {
    printf("Close\n");
}

microrl_t  rl;
microrl_t* prl = &rl;

void term_task(void* args) {

    init();
    // call init with ptr to microrl instance and print callback
    microrl_init(prl, print);
    // set callback for execute
    microrl_set_execute_callback(prl, execute);

#ifdef _USE_COMPLETE
    // set callback for completion
    microrl_set_complete_callback(prl, complet);
#endif
    // set callback for Ctrl+C
    microrl_set_sigint_callback(prl, sigint);
    while (1) {
        // put received char from stdin to microrl lib
        microrl_insert_char(prl, get_char());
    }
}

int main(int argc, char* argv[]) {
    osKernelInitialize();

    sem = xSemaphoreCreateBinary();

    RingBuffer_Init(&rbuff, inputBuff, sizeof(uint8_t), 512);

    TCPApplication app;
    app.cli.closedCallback = term_close;
    app.cli.recvCallback   = term_recv;
    app.maxOfConns         = 1;
    app.poolOfConns        = &conn;
    app.port               = 8022;
    app.timeout_sec        = 60;

    TCPServer_Init("term", &app);

    osThreadAttr_t thattr;
    thattr.name = "microrl";
    osThreadNew(term_task, NULL, &thattr);

    osKernelStart();

    return 0;
}
