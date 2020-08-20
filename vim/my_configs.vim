"--------------------Plugin-------------------"
set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
"------------------My Plugin-----------------"
Plugin 'Valloric/YouCompleteMe'
Plugin 'mileszs/ack.vim'
Plugin 'fatih/vim-go'
Plugin 'SirVer/ultisnips'
Plugin 'universal-ctags/ctags'
Plugin 'vim-scripts/taglist.vim'
Plugin 'Yggdroot/indentLine'
Plugin 'pangloss/vim-javascript'
Plugin 'rhysd/vim-clang-format'
"--------------------------------------------"
call vundle#end()            " required
filetype plugin indent on    " required

"-------------------快捷输入-----------------"
" autocmd BufNewFile,BufRead *.h,*.cpp inoremap {} <CR>{<CR>}<Up><Right><CR>
" autocmd BufNewFile,BufRead *.js inoremap {} <SPACE>{<CR>}<esc><Up>o
" autocmd BufNewFile,BufRead *.h,*.cpp inoremap #inc #include<SPACE>

"---------------------Make-------------------"

" python
autocmd BufNewFile,BufRead *.py map <F5> :! python %:p<CR>

" C++
autocmd BufNewFile,BufRead *.cpp map <F5> :! g++ -std=c++1z %:p -O3 -o out -g -lpthread<CR>:! %:p:h/out<CR>

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
let g:ycm_key_list_stop_completion = ['<enter>']
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
"高亮搜索关键词
let g:ackhighlight = 1
"在QuickFix窗口使用快捷键以后，自动关闭QuickFix窗口
let g:ack_autoclose = 1
"使用ack的空白搜索，即不添加任何参数时对光标下的单词进行搜索，默认值为1，表示开启，置0以后使用空白搜索将返回错误信息
let g:ack_use_cword_for_empty_search = 1

"---------------------indentLine------------------"
"json文件显示引号并且禁用这个插件
autocmd Filetype json let g:indentLine_enabled = 0

"---------------------ClangFormat-----------------"
let g:clang_format#code_style = "google"
let g:clang_format#auto_format = 1
" let g:clang_format#auto_format_on_insert_leave = 1

"---------------------NerdTree--------------------"
let g:NERDTreeWinPos = "left"
" 最后一个窗口是nerdtree时，关闭
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

"检查是否已经打开tree
function! IsNERDTreeOpen()
  return exists("t:NERDTreeBufName") && (bufwinnr(t:NERDTreeBufName) != -1)
endfunction

"如果已经打开，那么关闭，如果没有打开，查找当前文件目录为根目录
function! SmartOpenTree()
  if !IsNERDTreeOpen()
    NERDTreeFind
  else
    NERDTreeToggle
  endif
endfunction

"实现F3一键开关功能
map <F3> :call SmartOpenTree()<cr>

"---------------------bigo-format------------------"
set autoread
autocmd BufNewFile,BufRead *.cpp,*.h,*.hpp map <F6> :!bigo-format %:p<CR>
autocmd BufNewFile,BufRead *.c,*.proto,*.xml map <F6> :!clang-format -i %:p<CR>

"---------------------other------------------"
set number
"ale插件有bug，必须使用这个值才能正常使用鼠标
set mouse=a 
let g:ycm_global_ycm_extra_conf = '/Users/bailiyang/.ycm_extra_conf.py'
" set fileencodings=ucs-bom,utf-8,utf-16,gbk,big5,gb18030,latin1

"修复ycm报错
if has('python3')
  silent! python3 1
endif
"控制缩进为2空格
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
"默认不折叠代码
set nofoldenable
"html不显示warnings
let g:syntastic_html_tidy_quiet_messages = { "level" : "warnings" }

"---------------------自动注释------------------"
autocmd BufNewFile *.h,*.hpp,*.c,*.cpp,Makefile,CMakeLists.txt,*.sh,*.lua,*.py exec ":call SetTitle()" 

" C语言风格注释 
func! SetComment_c()
	call setline(1,"/*") 
	call append(line("."), "*   文件名称：".expand("%:t")) 
	call append(line(".")+1, "*   创 建 者：bailiyang")
	call append(line(".")+2, "*   创建日期：".strftime("%Y年%m月%d日")) 
	call append(line(".")+3, "*/") 
	call append(line(".")+4, "")
endfunc

" shell风格注释
func! SetComment_sh()
	call setline(3, "#   文件名称：".expand("%:t")) 
	call setline(4, "#   创 建 者：bailiyang")
	call setline(5, "#   创建日期：".strftime("%Y年%m月%d日")) 
	call setline(6, "")
endfunc 

" lua风格注释
func! SetComment_lua()
	call setline(3, "--   文件名称：".expand("%:t")) 
	call setline(4, "--   创 建 者：bailiyang")
	call setline(5, "--   创建日期：".strftime("%Y年%m月%d日")) 
	call setline(6, "")
endfunc 

" 定义函数SetTitle，自动插入文件头 
func! SetTitle()
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
  elseif &filetype == 'python'
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
    "处理hpp头文件
    if expand("%:e") == 'hpp' 
      call append(line(".")+5, "#ifndef _".toupper(expand("%:t:r"))."_HPP") 
      call append(line(".")+6, "#define _".toupper(expand("%:t:r"))."_HPP") 
      call append(line(".")+7, "")
      call append(line(".")+8, "")
      call append(line(".")+9, "#endif //".toupper(expand("%:t:r"))."_HPP") 
    "处理h头文件
    elseif expand("%:e") == 'h' 
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

