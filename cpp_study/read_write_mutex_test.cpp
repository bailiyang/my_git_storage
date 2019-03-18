/*
*   文件名称：test.cpp
*   创 建 者：bailiyang
*   创建日期：2018年09月04日
*/

#include <iostream>
#include <vector>
#include <map>
#include <thread>
#include <unordered_set>
#include <mutex>
#include <atomic>
#include <condition_variable>
#include <sys/time.h>
#include <stdlib.h>
#include <unistd.h>

#define PRINT_FUN() (Test::Foo(__FUNCTION__))

class Test
{
  public:
    static void Foo(std::string st)
    {
      printf("%s\n", __FUNCTION__);
    };
};

class ReadWriteMutex
{
  public:
    ReadWriteMutex()
    {
      write_flag_.store(false);
      read_thread_.store(0);
    }

    void ReadLock()
    {
      while (write_flag_.load() == true)
        std::this_thread::sleep_for(std::chrono::microseconds(50));
      read_thread_++;
    }

    void ReadUnlock()
    {
      read_thread_--;
    }

    void WriteLock()
    {
      while (write_flag_.load() == true)
        std::this_thread::sleep_for(std::chrono::microseconds(50));

      write_flag_.store(true);
      while (read_thread_ != 0)
        std::this_thread::sleep_for(std::chrono::microseconds(50));
    }

    void WriteUnlock()
    {
      write_flag_.store(false);
    }

  private:
    std::atomic<bool> write_flag_;
    std::atomic<int> read_thread_;
};

typedef std::map<std::string, uint64_t> Map;
ReadWriteMutex read_write_mutex;
std::mutex mutex;
std::atomic<uint64_t> stat;
Map map;

Map::iterator GetIter(const std::string &name)
{
  stat++;
  read_write_mutex.ReadLock();
  auto iter = map.find(name);
  read_write_mutex.ReadUnlock();

  if (iter == map.end())
  {
    read_write_mutex.WriteLock();
    map.insert(std::make_pair(name, 0));
    read_write_mutex.WriteUnlock();
    return map.find(name);
  }
  else
    return iter;
}

void Run()
{
  srand(time(NULL) + getpid());
  const std::string head = "test_";
  for (;;)
  {
    std::string name = head + std::to_string(rand() % 1000); 
    GetIter(name)->second++;
  }
}

void Swap()
{
  while(true)
  {
    /* std::lock_guard<std::mutex> lock(mutex); */
    Map temp_map;
    read_write_mutex.WriteLock();
    map.swap(temp_map);
    printf("set size %lu\n", temp_map.size());
    printf("stat %lu\n", stat.load());
    stat.store(0);
    read_write_mutex.WriteUnlock();
    std::this_thread::sleep_for(std::chrono::seconds(3));
  }
}

int main(int argc, char *argv[])
{
  std::unordered_set<uint64_t> vec;
  std::vector<std::thread> thread_vec;
  for (int i = 0; i < 100; i++)
    thread_vec.push_back(std::thread(Run));
  Swap();
  return 0;
}
