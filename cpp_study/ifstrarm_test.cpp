#include <fstream>
#include <iostream>
#include <vector>
#include <stdio.h>

std::vector <std::string> st;

std::ifstream& open_read(std::string ifile){
    std::ifstream in(ifile);
    std::string line;
    if (in.is_open()){      //先判断文件流是否正确打开
        while (!in.eof()){      //读入文件直到结尾
            getline(in,line);       //按行读取，pushback到vector中
            st.push_back(line);
        }
    }
    in.close();     //关闭流
    std::cout << "read OK" << std::endl;
}

std::ofstream& open_write(std::string ofile){
    std::ofstream out(ofile, std::ofstream::app);
    if (out.is_open()) {        //与读入一致，改为循环输出
        for (auto it : st) {
            out << it << std::endl;
        } 
    }
    out.close();
    std::cout << "write OK" << std::endl;
}

int main(int argc, char *argv[])
{
    open_read("./data_in");
    open_write("./data_out");
    return 0;
}

