#include <initializer_list>
#include <iostream>

using namespace std;

int add(initializer_list<int> st){      //用initializer_list类型作为形参，注意要加入std::类似string
    int ans = 0;
    for (const auto &elem : st){        //用范围for语句通过引用方式遍历list中元素
        ans = ans + elem;               //累加
    }
    return ans;
}

int main(int argc, char *argv[])
{
    int a = 100;
    int b = 100;

    std::cout << add({a,b,a,a,a}) << std::endl;     //这里可以在大括号内使用任何数量的int类型参数，均能正确得到累加值
    return 0;
}
