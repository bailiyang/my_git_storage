#include <iostream>
#include <cstring>
#include <unistd.h>
#include <errno.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <arpa/inet.h>

class Client
{
    public:
        Client() = default;
        ~Client() = default;
        int Init()
        {
            socket_fd = socket(AF_INET, SOCK_STREAM, 0);
            if (socket_fd < 0)
            {
                printf("create socket failed errno %d\n", errno);
                return -1;
            }
            
            struct sockaddr_in addr;
            bzero(&addr, sizeof(sockaddr_in));
            addr.sin_family = AF_INET;
            addr.sin_port = htons(22);
            if (inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr) < 0)
            {
                printf("handle inet_addr failed, errno %d\n", errno);
                return -1;
            }
            printf("ip %s\n", inet_ntoa(addr.sin_addr));

            if (connect(socket_fd, (sockaddr *)&addr, sizeof(struct sockaddr)) < 0)
            {
                printf("bind socket failed errno %d\n", errno);
                return -1;
            }

            return 0; 
        }

        int Send(std::string st = "Hello World")
        {
            auto send_byte = send(socket_fd, st.c_str(), st.size(), 0);
            if (send_byte < 0)
            {
                printf("send failed, errno %d\n", errno);
                return -1;
            }
            else if (send_byte != st.size())
            {
                printf("send not all message, only send %ld byte, should send %ld byte", send_byte, st.size());
                return -1;
            }
            printf("send success, send byte %ld", send_byte);
            return 0;
        }

        void Close()
        {
            close(socket_fd);
        }

    private:
        int socket_fd;
};

int main(int argc, char *argv[])
{
    Client client;
    client.Init();
    client.Send();
    sleep(1);
    client.Close();
    /* client.start(); */
    return 0;
}
