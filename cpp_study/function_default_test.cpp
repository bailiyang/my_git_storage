#include <iostream>
#include <string>

using namespace std;

string make_plural(const string a, const string b = "s"){       //这里形参b使用了默认值s，在没有输入b的情况下，就会使用默认值初始化这个形参，如果有实参，会用实参初始化
    return a + b;
}

int main(int argc, char *argv[])
{
    std::cout << make_plural("string") << std::endl;        //使用默认值初始化形参b
    std::cout << make_plural("a","b") << std::endl;     //使用实参初始化形参a与b
    std::cout << make_plural("e") << std::endl; 
    return 0;
}
