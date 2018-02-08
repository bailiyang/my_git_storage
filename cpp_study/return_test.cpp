#include <iostream>
#include <string>

using namespace std;

bool f(int a,int b){
    if (a == b){
        return a == b;
    }
    if (a < b){
        return a < b;       //这里return一定要有bool类型值返回，或能转换成bool类型的值
    }
    //这里缺少了一条return的代码，如果a>b时，没有返回值，则该错误是不可预知的错误，返回值不确定
}

int main(int argc, char *argv[])
{
    int a = 300;
    int b = 200;

    std::cout << f(a,b) << std::endl;
    return 0;
}
