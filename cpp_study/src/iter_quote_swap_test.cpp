#include <iostream>

using namespace std;

void swap(int x, int y){
    int temp;
    temp = x;
    x = y;
    y = temp;
    return;
}

void swap_iter(int* x, int* y){
    int temp;
    printf("a=%d, b=%d\n",*x, *y);
    temp = *x;
    *x = *y;
    *y = temp;
    return;
}

void swap_quote(int &x, int &y){
    int temp;
    temp = x;
    x = y;
    y = temp;
    return;
}

int main(int argc, char *argv[])
{
    int a = 10;
    int b = 20;
    swap(a, b); //普通传参，不改变a、b值
    std::cout << "a=" << a << " b=" << b << std::endl;
    swap_iter(&a, &b);  //指针传参，需要传入a、b的地址（&取地址符），改变的是指针指向，间接改变了a与b的值
    std::cout << "a=" << a << " b=" << b << std::endl;
    swap_quote(a, b);   //引用传参，不需要传入a与b的地址（&这里是引用符号），由于函数不是“copy”了一份a与b，就是处理原先的a与b，因此直接改变了a与b的值
    std::cout << "a=" << a << " b=" << b << std::endl;
    return 0;
}
