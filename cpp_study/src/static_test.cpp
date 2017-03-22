#include <iostream>

using namespace std;

void func_static(){
    static int temp = 5;
    temp ++;
    std::cout << temp << std::endl;
}

void func(){
    int temp = 5;
    temp ++;
    std::cout << temp << std::endl;
}

int main(int argc, char *argv[])
{
    for (auto i = 0;i < 10; ++ i) {
        func_static();
    }
    std::cout << "\n" << std::endl;
    for (auto i = 0;i < 10; ++ i) {
        func();
    }
    return 0;
}
