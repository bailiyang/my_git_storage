#include <iostream>
#include <string>

class Screen{
    public:
        typedef std::string::size_type pos;
        Screen() = default;     //如果没有参数，默认初始化
        Screen(pos w);      //重载初始化函数，初始化为一个给定长度的空串
        Screen(pos w, std::string text);        //重载版本2，初始化为一个给定长度的字符串

        char get(pos j);        //获取j位置的字符的函数
        char get();     //重载函数，获取焦点位置字符
        
        inline Screen &move(pos j);       //移动焦点的函数
        inline Screen &set(char c);     //放置字符串到当前焦点
        inline Screen &set(int i, char c);      //重载版本，在指定位置放置
         
        inline Screen &display(std::ostream &os){       //内连输出函数
            do_display(os);
            return *this;
        }

    private:
        void do_display(std::ostream &os){      //私有的输出函数
            os << contens;
        }
        pos width = 0;      //成员，字符串宽度
        pos focus = 0;      //成员，焦点
        std::string contens;        //成员，字符串的值
};
