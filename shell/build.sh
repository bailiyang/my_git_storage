#!/bin/bash
command=$1

file_index=`pwd`
#判断是否已经在src目录下
if [ "${file_index:0-3}" == "src" ]
then
    cd ../
    file_index=`pwd`
fi

#判断是否已经在bin目录下
if [ "${file_index:0-3}" == "bin" ]
then
    cd ../
    file_index=`pwd`
fi

#判断是否已经在build目录下
if [ "${file_index:0-5}" != "build" ]
then
    #判断当前目录是否存在build目录
    if [ -d "${file_index}/build" ]
    then
        #已经存在，删除旧的，再创建新的
        rm -rf ./build
    fi
    mkdir build
    cd build
fi

if [ "$command" = "help" -o "$command" = "h" -o "$command" = "-h" -o "$command" = "--help" ]
then
    echo "方便的编译工具"
    echo "   命令参数                      作用"
    echo "     ycm          在项目目录下生成ycm需要的补全json文件"
    echo "    无参数        编译当前项目"
    echo "help/h/--help/-h  帮助"
    exit
fi

if [ "$command" = "ycm" ]
then
    cmake ../ -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
    compdb -p . list > tmp_compile_commands.json
    mv ./tmp_compile_commands.json ../compile_commands.json
    echo "生成compile_commands.json完毕"
    exit
fi

if [ ! -d "$command" ]
then
    cmake ../
    make -j2
    exit
fi

