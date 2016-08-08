#include <iostream>

using namespace std;

istream& read (istream &os){
    string st;   
    int loop (0);   
    while ((os >> st) && (!os.eof())){     //每次读取，直到文件结尾,这里要判断两个值，才能先读取再判断是否为结尾，注意顺序
        std::cout << st << std::endl;
    }
    os.clear();     //流复位
    return os;
}

int main(int argc, char *argv[])
{
    read(cin);
    return 0;
}
