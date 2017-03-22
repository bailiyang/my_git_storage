#include <iostream>
#include <ctime>

using namespace std;

class line
{
    public:
        static int objectCount;

        static int getCount()
        {
            return objectCount;
        }

        static void setCount(int count)
        {
            objectCount = count;
        }

        line()
        {
            this->objectCount ++;
            std::cout << "init line success objectCount = " <<this->objectCount << std::endl;
        }

    private:
        static int lenth;
};


int line::objectCount = 0;

int main(int argc, char *argv[])
{
    line temp;
    line *ptr;
    ptr = &temp;
    line::setCount(100);
    std::cout << line::getCount() << std::endl;
}
