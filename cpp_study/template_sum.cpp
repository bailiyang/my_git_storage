#include <iostream>
#include <map>
#include <vector>
#include <memory>
#include <algorithm>
#include <string>
#include <cstring>
#include <unordered_map>

template <typename T>
auto sum(T begin, T end) -> typename std::remove_reference<decltype(*begin)>::type
{
    typename std::remove_reference<decltype(*begin)>::type res = 
        typename std::remove_reference<decltype(*begin)>::type();
    for (auto iter = begin; iter != end; iter ++)
    {
        res += *iter;
        std::cout << *iter << std::endl;
    }
    return res;
}

int main(int argc, char *argv[])
{
    std::vector<long> vec = {1,2,3,4,5};
    std::cout << sum(vec.begin(), vec.end()) << std::endl;
}
