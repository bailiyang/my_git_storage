#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char *argv[])                                              
{
    std::vector<int> vec = {1,2,3,4,5,6,1,20,3,44,1,2,3,5,7534,4,456,3,345,4,7,8,9,0};

    int num = 0;
    auto comm = [num](const int a)
    {
        if (a > num) return true;
        else return false;
    };

    //排序
    sort(vec.begin(), vec.end());
    //去重
    auto end_uniq = unique(vec.begin(), vec.end());
    //删除重复
    vec.erase(end_uniq, vec.end());
    //找到第一个大于num的值
    auto pos = find_if(vec.begin(), vec.end(), comm);
    //打印所有大于num的值
    for_each(vec.begin(), vec.end(), 
            [num](const int &inc)
            {
                if (inc > num)
                    std::cout << inc << " ";
            }
            );
}

