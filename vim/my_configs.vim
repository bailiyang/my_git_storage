"--------------------Plugin-------------------"
filetype on

set rtp+=~/.vim/bundle/Vundle.vim
"------------------My Plugin-----------------"
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'mileszs/ack.vim'
Plugin 'fatih/vim-go'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'universal-ctags/ctags'
Plugin 'vim-scripts/taglist.vim'
call vundle#end()            " required
filetype plugin indent on    " required

"-------------------快捷输入-----------------"
autocmd BufNewFile,BufRead *.h,*.cpp inoremap {} {<CR>}<esc><Up>o
autocmd BufNewFile,BufRead *.h,*.cpp inoremap #inc #include<SPACE>

"---------------------Make-------------------"

" python
autocmd BufNewFile,BufRead *.py map <F5> :! python %:p<CR>

" C++
autocmd BufNewFile,BufRead *.cpp map <F5> :! g++ -std=c++11 %:p -o out.exe -g -lpthread<CR>:! %:p:h/out.exe<CR>

" Go
autocmd BufNewFile,BufRead *.go map <F5> :GoRun<CR>

" Shell
autocmd BufNewFile,BufRead *.sh map <F5> :! /bin/bash %:p<CR>

" lua
autocmd BufNewFile,BufRead *.lua map <F5> :! /usr/bin/lua %:p<CR>

"---------------------YCM--------------------"
"输入完毕后，自动关闭顶端草稿提示
" let g:ycm_autoclose_preview_window_after_completion = 1
"补全函数时，显示原型函数
let g:ycm_add_preview_to_completeopt = 1
"不会自动关闭顶端函数提示，而是在退出插入模式后关闭提示窗口
let g:ycm_autoclose_preview_window_after_insertion = 1
"点击回车（默认为ctrl+y），强制关闭下拉提示菜单
let g:ycm_key_list_stop_completion = ['<tab>']
"触发全局函数补全
let g:ycm_key_invoke_completion = '<c-y>'

"选择性加载.ycm_extra_conf.py，而不是全部提示
let g:ycm_confirm_extra_conf  = 1
"全局conf
let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
"跳转
nnoremap <c-g> :YcmCompleter GoTo<CR>
"显示实际类型
nnoremap <c-t> :YcmCompleter GetTypeImprecise<CR>
"自动修复语义
nnoremap <c-x> :YcmCompleter FixIt<CR>
"静态代码检查
nmap <F6> :YcmDiags<CR>

"---------------------UltiSnips------------------"
"使用ctrl+j补全格式
let g:UltiSnipsExpandTrigger="<c-j>"
"使用ctrl+right下一个可以填写的项
let g:UltiSnipsJumpForwardTrigger="<C-Right>"
"使用ctrl+left上一个可以填写的项
let g:UltiSnipsJumpBackwardTrigger="<C-Left>"

let g:UltiSnipsSnippetDirectories = ['~/.vim/UltiSnips']
"let g:UltiSnipsEditSplit="vertical"

"---------------------Ack.vim------------------"
"没有参数，默认查找当前光标下词组
map <F2> :Ack!<CR>

"---------------------Ctags------------------"
" let g:ctags_statusline=1
set tags=tags;

"---------------------taglist------------------"
"不自动打开taglist
let Tlist_Auto_Open=0
"F4自动打开与关闭taglist
nmap <F4> :TlistToggle<CR>
"自动退出taglist
let Tlist_Exit_OnlyWindow = 1
"右侧显示
let Tlist_Use_Right_Window = 1
"只显示一个文件的list
let Tlist_Show_One_File = 1
"打开taglist时，焦点在list里
let Tlist_GainFocus_On_ToggleOpen = 1
"taglist宽度
let Tlist_WinWidth = 50

"---------------------other------------------"
set fileencodings=utf-8,gbk,utf-16le,cp1252,iso-8859-15,ucs-bom
set number
"ale插件有bug，必须使用这个值才能正常使用鼠标
" set ttymouse=xterm
set mouse=a 
"控制缩进为2空格
set tabstop=2
set softtabstop=2
set shiftwidth=2
set expandtab

"---------------------color------------------"
set nocompatible
syntax enable
colorscheme peaksea

"---------------------自动注释------------------"
if exists('g:my_title')
  finish
endif

autocmd BufNewFile *.h,*.c,*.cpp,Makefile,CMakeLists.txt,*.sh,*.lua,*.py exec ":call SetTitle()" 

" C语言风格注释 
func SetHeader_c()
	call setline(1,"/*") 
	call append(line("."), "*   文件名称：".expand("%:t")) 
	call append(line(".")+1, "*   创 建 者：bailiyang")
	call append(line(".")+2, "*   创建日期：".strftime("%Y年%m月%d日")) 
	call append(line(".")+3, "*/") 
	call append(line(".")+4, "")
endfunc

" shell风格注释
func SetHeader_sh()
	call setline(3, "#   文件名称：".expand("%:t")) 
	call setline(4, "#   创 建 者：bailiyang")
	call setline(5, "#   创建日期：".strftime("%Y年%m月%d日")) 
	call setline(6, "")
endfunc 

" lua风格注释
func SetHeader_lua()
	call setline(3, "--   文件名称：".expand("%:t")) 
	call setline(4, "--   创 建 者：bailiyang")
	call setline(5, "--   创建日期：".strftime("%Y年%m月%d日")) 
	call setline(6, "")
endfunc 

" 定义函数SetTitle，自动插入文件头 
func SetTitle()
  "处理make、cmake
	if &filetype == 'make' 
		call setline(1,"") 
		call setline(2,"")
		call SetHeader_sh()
 
  "处理shell
	elseif &filetype == 'sh' 
		call setline(1,"#!/bin/bash") 
		call setline(2,"")
		call SetHeader_sh()

  "处理python
  elseif &filetype == 'python'
		call setline(1,"#!/usr/bin/python") 
		call setline(2,"#-*- coding:utf-8 -*-")
		call SetHeader_sh()

  "处理lua
  elseif expand("%:e") == 'lua' 
		call setline(1,"#!/usr/bin/lua") 
		call setline(2,"")
		call SetHeader_lua()
		
  "处理c、c++
	else
	  call SetHeader_c()
    "处理h头文件
	  if expand("%:e") == 'h' 
      call append(line(".")+5, "#ifndef _".toupper(expand("%:t:r"))."_H") 
      call append(line(".")+6, "#define _".toupper(expand("%:t:r"))."_H") 
      call append(line(".")+7, "")
      call append(line(".")+8, "")
      call append(line(".")+9, "#endif //".toupper(expand("%:t:r"))."_H") 

    "处理.c文件
    elseif &filetype == 'c' 
      call append(line(".")+5,"#include \"".expand("%:t:r").".h\"") 
    "处理.cpp文件
    elseif &filetype == 'cpp' 
      call append(line(".")+5, "#include \"".expand("%:t:r").".h\"") 
    endif
	endif
endfunc

let g:my_title = 1

