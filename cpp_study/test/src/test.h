#include <iostream>

class Cls
{
    public:
    static const int Size = 10;
};

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
