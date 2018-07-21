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
"--------------------------------------------"
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
set ttymouse=xterm
set mouse=a 
