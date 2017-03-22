#include <iostream>
#include <ctime>

using namespace std;


int main(int argc, char *argv[])
{
    time_t time_now = time(0);

    struct tm *time_tm = localtime(&time_now);
    std::clog << time_tm->tm_hour << std::endl;
}
