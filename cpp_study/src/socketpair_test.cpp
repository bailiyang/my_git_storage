#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
#include <error.h>

#define BUF_SIZE 50
int main(int argc, char *argv[])                                              
{
    int sv[2];
    const char* string = "test";
    char* buf = (char*)calloc(1, BUF_SIZE);
    pid_t pid;

    if (socketpair(AF_UNIX,SOCK_STREAM, 0, sv) == -1)
    {
        printf("socketpair init rerror\n");
        exit(-1);
    }

    pid = fork();
    if (pid == 0)
    {
        printf("father process pid is %d\n", pid);
        close(sv[0]);
    }
    else if (pid > 0)
    {
        printf("children process create, pid is %d\n", pid);
        close(sv[1]);
        if (-1 == write(sv[0], string, strlen(string)))
        {
            printf("write to socket error");
            exit(-1);
        }
        printf("father process %d send socketpair success\n", getpid());
    }


    if (pid == 0)
    {
        if (-1 == read(sv[1], buf, BUF_SIZE))
        {
             printf("Pid %d read from socket error:%s\n",getpid(), strerror(errno));
            exit(-1);
        }
        printf("Pid %d read string in same process : %s \n",getpid(), buf);
        printf("Test successed , %d\n",getpid());
    }
    for (;;)
    {

    }
}

