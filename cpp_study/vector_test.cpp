#include <vector>
#include <iostream>

using namespace std;

vector<int> list = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

bool vector_find(vector<int>::iterator find_begin, vector<int>::iterator find_end, int find_num ){
    int val = 0;
    if (find_begin <= list.begin()){        //判断begin是否合法，不合法丢弃
        while (find_begin < list.end()){        //遍历处理指定范围元素
            val = *find_begin;
            if (val == find_num){       //判断是否是目标值
                return true;
            }
            find_begin++;       //不是则next
        }
    }
    return false;
}

int main(int argc, char *argv[])
{
    auto begin = list.begin();
    auto end = list.end();
    int num;
    std::cout << "input num you want to find" << std::endl;
    std::cin >> num;

    std::cout << vector_find(begin, end, num) << std::endl;
    return 0;
}
