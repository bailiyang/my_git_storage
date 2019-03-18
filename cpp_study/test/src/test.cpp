/*
*   文件名称：test.cpp
*   创 建 者：bailiyang
*   创建日期：2018年10月16日
*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <string>
#include <cstring>

void foo(std::vector<int> &vec)
{
  if (vec.empty())
    std::cout << "empty" << std::endl;
  else
  {
    for (const auto &iter : vec)
      std::cout << iter << std::endl;
  }
}

int main(int argc, char *argv[])
{
  std::vector<int> vec{1,2,3};
  auto iter = vec.begin();
  for (iter = vec.begin(); iter != vec.end();iter++)
  {
    if (*iter == 2)
      break;
  }

  for (;iter != vec.end(); iter++)
    printf("%d\n", *iter);
  return 0;
}
