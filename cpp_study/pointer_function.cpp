#include <vector>
#include <iostream>

using namespace std;

int add(int a, int b){
    return a + b;       //这是原函数
}

int main(int argc, char *argv[])
{
    int (*f)(int, int);     //这是函数指针，形参列表需要跟原函数一致
    f = add;        //等价于typedef命令，另f指向add函数
    std::cout << f(1,2) << std::endl;       //f（1,2）等价于add（1,2），实际调用的是（*f）（1,2）
    
    std::vector<decltype(f)> v;     //这里因为指针是指向函数的，因此需要用decltype让其与f类型一致
    v.push_back(f);     //这样才能存入f

    for (auto i : v){
        std::cout << (void*)i << std::endl;
    }
    return 0;
}
