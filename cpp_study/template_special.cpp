#include <iostream>
#include <map>
#include <vector>
#include <memory>
#include <algorithm>
#include <string>
#include <cstring>
#include <unordered_map>

template <typename T>
void print(const T s)
{
    printf("use T\n");
    std::cout << s << std::endl;
}

template <typename T>
void print(T *s)
{
    printf("use T*\n");
    std::cout << *s << std::endl;
}

template <>
void print(const char *s)
{
    printf("use char *\n");
    std::cout << std::string(s) << std::endl;
}

int main(int argc, char *argv[])
{
    const std::string *st = new std::string("hello world"); 
    print(std::string("hello world"));
    print(st);
    print("123");
}
