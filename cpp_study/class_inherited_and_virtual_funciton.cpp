#include <iostream>
#include <ctime>

using namespace std;

class father_class
{
    public:
        virtual int getLenth() = 0;

        void setLenth(int len){
            this->lenth = len;
        }
    protected:
        int lenth;
};


class child_class: public father_class{
    //继承父类，可以使用父类方法
    public:
        void swap(int &a, int &b){
            int temp;
            temp = a;
            a = b;
            b = temp;
        }

        int getLenth()
        {
            std::cout << "this is virtual function, lenth = " << this->lenth << std::endl;
            return this->lenth;
        }

        int operator + (child_class &f){
            child_class temp;
            temp.setLenth(this->getLenth() + f.getLenth());
            return temp.getLenth();
        }

};

int main(int argc, char *argv[])
{
    child_class f;
    f.setLenth(10);
    printf("lenth is %d\n", f + f);
    int a = 10;
    int b = 20;
    f.swap(a, b);
    printf("swap result is a = %d, b = %d\n", a, b);
}

