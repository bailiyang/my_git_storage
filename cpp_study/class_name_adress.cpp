#include "./class_name_adress.h"

using namespace std;

int main(int argc, char *argv[])
{
    person st;      //实例化一个新person对象
    if ( std::cout << "input name and adress" << std::endl ){
        st.read(cin, st);
    }       //输入到st的name与adress成员中
    if ( std::cout << "name and adress is \n" << std::endl ){
        st.print(cout, st);
    }       //使用print成员函数直接输出
    std::cout << "\n" << st.check() << std::endl;     //使用check成员函数输出
    return 0;
}
