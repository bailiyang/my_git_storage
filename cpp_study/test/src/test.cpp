#include <iostream>
#include <map>
#include <vector>
#include <memory>
#include <algorithm>
#include <string>
#include <cstring>
#include <unordered_map>

struct Test
{
    std::string a;
    std::string b;
    std::string c;

    bool operator == (const Test& other)
    {
        return (a == a && b == b && c == c);
    }
};

int main(int argc, char *argv[])                                              
{
    bool bl = 2;
    std::cout << bl << std::endl;
}


