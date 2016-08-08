#include<string>
#include<iostream>

using namespace std;

struct person{      //定义一个类，struct是默认public的，class默认为private
    string name;       //类的成员
    string adress;
    
    public:
    string check() const{        //成员函数，this关键字总是指向“这个”类
        return "name is : " + this->name + "\n" + "adress is : " + this->adress;
    }

    int read(std::istream &is, const person item){       //使用istream类型输入，尽量通用的使用输入
        if ( is >> this->name >> this->adress ) {       
            return 1;
        }
        else 
            return -1;
    }

    int print(std::ostream &os, const person item){      //同上
        if ( os << "name is :" << this->name << " adress is : " << this->adress) {
            return 1;
        }
        else
            return -1;
    }
};
