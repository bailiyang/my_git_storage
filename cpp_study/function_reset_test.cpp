#include <iostream>
#include <stdio.h>

using namespace std;

void reset(int &n){     //清零功能的函数，形参为引用
    n = 0;
}

void change(int &a,int &b){     //交换功能的函数，引用形参
    int c;
    c = a;
    a = b;
    b = c;
}

int main()
{
    int a,b;
    std::cout << "input a" << std::endl;
    std::cin >> a;
    std::cout << "input b" << std::endl;
    std::cin >> b;

    change(a,b);
    std::cout << a << "\n" << b << std::endl;
    return 0;
}
