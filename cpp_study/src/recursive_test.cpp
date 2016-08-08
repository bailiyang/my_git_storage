#include <vector>
#include <iostream>

using namespace std;

void read(const vector<int> &st ,decltype(st.begin()) n){       //这里为了递归，使用了对vector类型的引用，这样不用再次拷贝多个副本了，n是递归次数，这里使用的是指针
    if (n < st.end()){      //递归退出条件
        std::cout << *n << std::endl;
        read(st,n+1);       //这里再次调用下一个，递归调用
    }
}

int main(int argc, char *argv[])
{
    std::vector<int> st = {1,2,3,4,5};
    read(st,st.begin());
    return 0;
}
