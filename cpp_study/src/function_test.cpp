#include <stdio.h>
#include <iostream>
#include <stdexcept>

using namespace std;

int fac(int num){       //简单的阶乘函数
    int res = 1;
    for (auto i = 1; i <= num ; ++i) {
        res = res * i;
    }
    return res;
}

int main(int argc, char *argv[])
{
    long n;
    std::cout << "input n" << std::endl;
    std::cin >> n;      //输入n
    try{
        if (n > 10) {       //判断是否过大，过大抛出异常
            throw runtime_error("n is too large");
        }
    }
    catch(runtime_error err){       //处理异常并重新键入n
        std::cout << err.what() << "\ninput another n" << std::endl;
        std::cin >> n;
    }

    std::cout << fac(n) << std::endl;       //调用函数

    return 0;
}
