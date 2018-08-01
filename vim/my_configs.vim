"--------------------Plugin-------------------"
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
"------------------My Plugin-----------------"
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'mileszs/ack.vim'
Plugin 'fatih/vim-go'
Plugin 'SirVer/ultisnips'
call vundle#end()            " required
filetype plugin indent on    " required

"-------------------快捷输入-----------------"
autocmd BufNewFile,BufRead *.h,*.cpp inoremap {} <CR>{<CR>}<Up><Right><CR>
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
let g:ycm_autoclose_preview_window_after_completion = 1
"点击回车（默认为ctrl+y），强制关闭下拉提示菜单
let g:ycm_key_list_stop_completion = ['<tab>']
"触发全局函数补全
let g:ycm_key_invoke_completion = '<c-y>'

"选择性加载.ycm_extra_conf.py，而不是全部提示
let g:ycm_confirm_extra_conf  = 1
let g:ycm_extra_conf_globlist  = ['/build/push/kiev/src/*', '!~/*']
"跳转
nnoremap <c-g> :YcmCompleter GoTo<CR>
"显示实际类型
nnoremap <c-t> :YcmCompleter GetTypeImprecise<CR>
"自动修复语义
nnoremap <c-x> :YcmCompleter FixIt<CR>
"静态代码检查
nmap <F4> :YcmDiags<CR>

"---------------------UltiSnips------------------"
"使用ctrl+j补全格式
let g:UltiSnipsExpandTrigger="<c-j>"
"使用ctrl+right下一个可以填写的项
let g:UltiSnipsJumpForwardTrigger="<C-Right>"
"使用ctrl+left上一个可以填写的项
let g:UltiSnipsJumpBackwardTrigger="<C-Left>"

"let g:UltiSnipsEditSplit="vertical"

"---------------------Ack.vim------------------"
"没有参数，默认查找当前光标下词组
map <F2> :Ack!<CR>

"---------------------other------------------"
set number
"ale插件有bug，必须使用这个值才能正常使用鼠标
" set ttymouse=xterm
set mouse=a 
"控制缩进为2空格
set tabstop=2
set softtabstop=2
set shiftwidth=2
set expandtab

"---------------------自动注释------------------"
autocmd BufNewFile *.h,*.c,*.cpp,Makefile,CMakeLists.txt,*.sh,*.lua,*.py exec ":call SetTitle()" 

" C语言风格注释 
func SetComment_c()
	call setline(1,"/*") 
	call append(line("."), "*   文件名称：".expand("%:t")) 
	call append(line(".")+1, "*   创 建 者：bailiyang")
	call append(line(".")+2, "*   创建日期：".strftime("%Y年%m月%d日")) 
	call append(line(".")+3, "*/") 
	call append(line(".")+4, "")
endfunc

" shell风格注释
func SetComment_sh()
	call setline(3, "#   文件名称：".expand("%:t")) 
	call setline(4, "#   创 建 者：bailiyang")
	call setline(5, "#   创建日期：".strftime("%Y年%m月%d日")) 
	call setline(6, "")
endfunc 

" lua风格注释
func SetComment_lua()
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
		call SetComment_sh()
 
  "处理shell
	elseif &filetype == 'sh' 
		call setline(1,"#!/bin/bash") 
		call setline(2,"")
		call SetComment_sh()

  "处理python
  elseif &filetype == 'py'
		call setline(1,"#!/usr/bin/python") 
		call setline(2,"#-*- coding:utf-8 -*-")
		call SetComment_sh()

  "处理lua
  elseif expand("%:e") == 'lua' 
		call setline(1,"#!/usr/bin/lua") 
		call setline(2,"")
		call SetComment_lua()
		
  "处理c、c++
	else
	  call SetComment_c()
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

