#include <iostream>
#include <vector>
#include <boost/shared_ptr.hpp>

class Data
{
    public:
        typedef std::shared_ptr<Data> DataPtr;
        Data(std::string imei, std::string content, std::string ext, int equence)
        {
            imei_ = imei;
            content_ = content;
            ext_ = ext;
            equence_ = equence; 
        }
        Data(std::string imei) : Data(imei, "", "", 0){};
        Data(std::string imei, std::string content) : Data(imei, content, "", 0){};
        Data(std::string imei, int equence) : Data(imei, "", "", equence){};
        Data(std::string imei, std::string content, std::string ext) : Data(imei, content, ext, 0){};
        
        std::string GetData()
        {
            std::string temp;
            temp += "imei:" + imei_;
            temp += " content:" + content_;
            temp += " ext:" + ext_;
            temp += " equence:" + std::to_string(equence_);
            return temp;
        }

    private:
        std::string imei_;
        std::string content_;
        std::string ext_;
        int equence_;
};


int main(int argc, char *argv[])
{
    std::vector<Data> list;
    list.push_back(Data("imei_0", 1));
    list.emplace_back("imei_1", 2);
    for (auto &iter : list)
    {
        std::cout << iter.GetData() << std::endl;
    }
    return 0;
}
