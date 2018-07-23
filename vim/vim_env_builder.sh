!#/bin/bash
#更新apt
sudo apt-get update
sudo apt-get -y upgrade

#c++编译环境
apt install gcc g++ make cmake open-ssl
apt install golang-go
apt install gcc-7 g++-7
apt install gcc-5 g++-5
apt install gcc-4.8 g++-4.8
#设置gcc版本切换
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 25
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 100
update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50

#go相关环境
apt remove golang-go
wget https://dl.google.com/go/go1.10.3.linux-amd64.tar.gzi /opt
tar -C /usr/local -xzf /opt/go1.10.3.linux-amd64.tar.gz
#go env
mkdir -p /build/go_path
echo "export GOROOT=/usr/local/go" >> ~/.bashrc
echo "export GOPATH=/build/go_path" >> ~/.bashrc
echo "export PATH=$PATH:$GOPATH:/usr/local/go/bin" >> ~/.bashrc

#python编译环境
apt install python3 python2.7
apt install python3-dev python2.7-dev
#设置python版本切换
update-alternatives --install /usr/bin/python python /usr/bin/python2.7 50
update-alternatives --install /usr/bin/python python /usr/bin/python3 100

#vim相关环境
apt install vim
apt install ack-grep
#amix/vimrc
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
#Vundle
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
#YouCompleteMe
git clone https://github.com/Valloric/YouCompleteMe.git ~/.vim/bundle/YouCompleteMe
python3 ~/.vim/bundle/YouCompleteMe/install.py --clang-completer --go-completer
#study
mkdir -p /build/study
git clone https://github.com/bailiyang/study.git /build/study
#复制vimrc文件
cp /build/study/vim/my_configs.vim ~/.vim_runtime
cp /build/study/vim/*.vim ~/.vim_runtime/vimrcs
rm --force ~/.vim_runtime/vimrcs/my_configs.vim
#用vundle安装其他插件
vim +PluginInstall -c quitall

