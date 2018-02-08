#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int a = 10;
    int b = 20;
    auto func = [&](int i){
        b = 10;
        return i * i;
    };
    std::cout << func(b) << std::endl;
    std::cout << b << std::endl;
    return 0;
}
