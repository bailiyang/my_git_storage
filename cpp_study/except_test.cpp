#include <stdexcept>
#include <stdio.h>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int a , b;
    std::cin >> a;
    std::cin >> b;
    
    try{
        if (b == 0) {                                      
           throw runtime_error("b = 0 , error");    //尝试执行，遇到错误抛出异常
        }
    }  
    catch (runtime_error err) {
        std::cout << err.what() << "\ntry another one b" << std::endl;      //处理上面抛出的runtime_error异常
        std::cin >> b;      //提示再次输入，重新获取被除数
    }
    
    std::cout << a / b << std::endl;        //异常处理完毕，直接输出值
    return 0;
}
