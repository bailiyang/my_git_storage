#include <iostream>

int big(int a, int* b){     //这里要传递int*指针类型，所以一定要设置为int*类型
    if (a > *b){        //由于要比较b指向的元素与a，所以进行解引用操作，得出的数值就是b指向的数字
        return a; 
    }
    else {
        return *b;
    }
}

int main(int argc, char *argv[])
{
    int a = 5;
    int c = 100;
    int* b = &c;
    std::cout << big(a,b) << std::endl;
    return 0;
}
