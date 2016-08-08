#include "./class_screen_test.h"

using namespace std;

Screen::Screen(pos w){
    string st(w, ' ');
    width = w;
}

Screen::Screen(pos w, std::string text){
    contens = text;
    width = w;
}

char Screen::get(pos j){
    return contens[j]; 
}

char Screen::get(){
    return contens[focus];
}

Screen &Screen::move(pos j){
    focus = j;
    return *this;
}

Screen &Screen::set(char c){
    contens[focus] = c;
    return *this;
}

Screen &Screen::set(int i, char c){
    contens[i] = c;
    return *this;
}


int main(int argc, char *argv[])
{
    string::size_type j = 10;    //定义size_type类的j，其实是一个int类型
    Screen s(j, "0123456789");      //使用版本2初始化，初始化为一个长度为10的字符串“0123456789”
    s.move(5).set('a').set(0, 'a');      //由于move/set的两个函数返回了*this，因此可以这样使用
    s.display(cout);        //输出全部字符串
    std::cout << "\n" << s.get() << std::endl;
    return 0;
}
