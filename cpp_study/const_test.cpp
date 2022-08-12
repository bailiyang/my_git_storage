#include <iostream>
#include <cctype>

using namespace std;

bool judge_letter(const std::string &s){        //判断是否为大写字母的函数，由于不需要改变s的值，应设为const string的引用，这样可以以const或者普通引用初始化
    for (auto i : s){
        if (std::isupper(i)){
            return true;
        }
    }
    return false;
}

std::string change_letter(std::string &s){     //替换s中的大写字母为小写，由于需要改变形参且影响实参，必须设为普通引用
    if (judge_letter(s)){
        for (auto &i : s) {
            if (std::isupper(i)){
                i = std::tolower(i);
            }
        }
        return "this is";
    }
   else return "error";
}

int main(int argc, char *argv[])
{
    string st;
    std::cout << "input st" << std::endl;
    std::cin >> st;
    
    std::cout << change_letter(st) << " " << st << std::endl;
    return 0;
}
