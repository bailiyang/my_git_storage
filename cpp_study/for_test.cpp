#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    std::vector<int> v_1 = {0,1,1,2};   //定义vector
    std::vector<int> v_2 = {1,1,1,2,3,4,5};
    auto v_min = v_1;
    auto v_max = v_2;
    auto min_size = v_1.end();      //假定最大队列、最小队列

    if (v_1.size() > v_2.size()) {      //如果不符合假定，设为正确的最大、最小值
        v_min = v_2;        
        v_max = v_1;
        min_size = v_2.end();
    }
    
    auto i = v_1.begin();
    auto j = v_2.begin();       //初始化控制循环的变量
    bool res = true;
    for ( ; i != min_size && j != min_size ; ++i , ++j) {       //循环至最小队列末尾
        if (*i != *j) {
            res = false;
            std::cout << "NO" << std::endl;
            return -1;      //判断是否为其头队列，有一处不对即停止运行并输出错误
        }
    }

    std::cout << "YES" << std::endl;
    return 0;
}
