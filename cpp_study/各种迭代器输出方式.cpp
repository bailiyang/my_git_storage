#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>

int main(int argc, char *argv[])                                              
{
    std::vector<int> vec = {1,2,3,4,5,6,7,8,9,0};
    auto func = [](int iter)
    {
        std::cout << iter << std::endl;
    };

    //使用ostream流迭代器输出
    std::ostream_iterator<int> out_iter(std::cout, "\n");
    copy(vec.begin(), vec.end(), out_iter);
    std::cout << std::endl;

    //调用for_each输出
    for_each(vec.begin(), vec.end(), func);
}

