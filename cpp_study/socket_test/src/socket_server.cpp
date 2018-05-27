#include <iostream>
#include <errno.h>
#include <cstring>
#include <unistd.h>
#include <sys/epoll.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unordered_set>

static const int Epoll_Size = 1024 * 128;

class Server
{
    public:
        Server() = default;
        ~Server()
        {
            close(socket_fd);
            close(epoll_fd);
        }

        int Init()
        {
            //创建socket
            socket_fd = socket(AF_INET, SOCK_STREAM, 0);
            if (socket_fd < 0)
            {
                printf("create socket failed errno %d\n", errno);
                return -1;
            }

            //创建addr(127.0.0.1:8888)
            struct sockaddr_in addr;
            addr.sin_family = AF_INET;
            int addr_num = inet_addr("127.0.0.1");
            if (addr_num < 0)
            {
                printf("handle inet_addr failed, errno %d\n", errno);
                return -1;
            }
            addr.sin_addr.s_addr = addr_num;
            printf("ip %s\n", inet_ntoa(addr.sin_addr));
            addr.sin_port = htons(8888);
            bzero(&addr.sin_zero, sizeof(addr.sin_zero));

            if (bind(socket_fd, (sockaddr *)&addr, sizeof(struct sockaddr)) < 0)
            {
                printf("bind socket failed errno %d\n", errno);
                return -1;
            }
            if (listen(socket_fd, 10) < 0)
            {
                printf("listen socket failed errno %d\n", errno);
                return -1;
            }

            //创建epoll
            epoll_fd = epoll_create(Epoll_Size);
            if (epoll_fd < 0)
            {
                printf("create epoll failed, errno %d\n", errno);
                return -1;
            }
            epoll_event event;
            event.data.fd = socket_fd;
            event.events = EPOLLIN|EPOLLET;
            epoll_ctl(epoll_fd, EPOLL_CTL_ADD, socket_fd, &event);
            printf("socket fd %d, epoll fd %d\n", socket_fd, epoll_fd);
            return 0;
        }

        void start()
        {
            for(;;)
            {
                epoll_event events[20];
                auto nfds = epoll_wait(epoll_fd, events, 20, 500); 
                printf("recv %d events from fd %d\n", nfds, epoll_fd);
                for (int i = 0; i < nfds; i++)
                {
                    printf("recv fd %d\n", events[i].data.fd);
                    //新连接
                    if (events[i].data.fd == socket_fd && events[i].events == EPOLLIN)
                        DoAccept();
                    else if (events[i].events & EPOLLIN)
                        DoRead();
                    else if (events[i].events & EPOLLOUT)
                        DoWrite();
                }
            }
        }

    private:
        int socket_fd;
        int epoll_fd;
        struct sockaddr_in clientaddr;
        std::unordered_set<int> hash_set; 

        //链接
        void DoAccept()
        {
            socklen_t client = sizeof(clientaddr);
            auto connfd = accept(socket_fd, (sockaddr *)&clientaddr, &client);
            if (connfd < 0)
            {
                printf("accept failed errno %d\n", errno);
                return;
            }

            epoll_event event;
            event.data.fd = socket_fd;
            event.events = EPOLLIN|EPOLLET;
            epoll_ctl(epoll_fd, EPOLL_CTL_ADD, connfd, &event);

            std::string addr_st = inet_ntoa(clientaddr.sin_addr);
            printf("recv addr %s accept, fd %d\n", addr_st.c_str(), connfd);
        }

        //读事件
        void DoRead()
        {
            char buf[1024];
            auto buflen = recv(socket_fd, buf, sizeof(buf), 0);
            if (buflen < 0)
            {
                printf("recv failed, errno %d", errno);
                return;
            }
            std::string recv_st(buf);
            printf("recv %s\n", recv_st.c_str());
        }

        //写事件
        void DoWrite()
        {

        }


};

int main(int argc, char *argv[])
{
    Server server;
    server.Init();
    server.start();
    return 0;
}
