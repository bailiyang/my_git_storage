#include <vector>
#include <list>
#include <iostream>
#include <string>

int main(int argc, char *argv[])
{
    std::vector<std::string> seq = {"a", "b", "c", "d", "e"}; 
    std::list<const char*> list = {"1", "2", "3"};      //初始化两个容器

    std::cout << "seq:" << std::endl;
    for (auto i : seq) std::cout << i << std::endl;
    std::cout << "list:" << std::endl;
    for (auto i : list) std::cout << i << std::endl;

    seq.assign(list.begin(), list.end());       //直接用assign赋值给seq，这里list值不会变化，seq会变为list中的数值，包括大小

    std::cout << "seq:" << std::endl;
    for (auto i : seq) std::cout << i << std::endl;
    std::cout << "list:" << std::endl;
    for (auto i : list) std::cout << i << std::endl;

    return 0;
}
