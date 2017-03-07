""""""""""""""""""""""""""快捷键设置"""""""""""""""""""""""
if has("unix")
    map ;c :e ~/.vimrc<CR>
elseif has("windows")
    map ;c :e $VIM/.vimrc<CR>
endif

map <F12> :source %:p<CR>
map ;b ^
map ;e $

map ;q :q<CR>
map ;Q :quitall<CR>
map ;w :w<CR>
map ;lw <C-W>l
map ;hw <C-W>h
map ;kw <C-W>k
map ;jw <C-W>j
map gl :b#<CR>
map gL <C-W>vgl
map gY gygL

map ;/ :nohls<CR>
map ; "
noremap ' ;

map <C-l> :tabnext<CR>
map <C-h> :tabprevious<CR>

func! Toggle_relative_nu()
    if getbufvar('', "&rnu") == 0
        set relativenumber
    else
        set norelativenumber
    endif
endfunc
map <F2> :call Toggle_relative_nu()<CR>

""""""""""""""""""""""""""MyPlugin"""""""""""""""""""""""
map <F11> :e /opt/cppenv/autoload/cppenv.vim<CR>


""""""""""""""""""""""""""Make"""""""""""""""""""""""

" python
autocmd BufNewFile,BufRead *.py map <F5> :! python %:p<CR>

" C
autocmd BufNewFile,BufRead *.c map <F7> :! gcc %:p -o out.exe -g -pthread<CR>
autocmd BufNewFile,BufRead *.c map <F5> <F7>:! %:p:h/out.exe<CR>

" C++
autocmd BufNewFile,BufRead *.cpp map <F7> :! g++ -std=c++11 %:p -o out.exe -g -pthread<CR>
autocmd BufNewFile,BufRead *.cpp map <F5> <F7>:! %:p:h/out.exe<CR>
autocmd BufNewFile,BufRead *.cpp map <F6> :! g++ -std=c++11 %:p -o out.exe -g -Wl,--whole-archive -lpthread -Wl,--no-whole-archive -static<CR>:! %:p:h/out.exe<CR>
autocmd BufNewFile,BufRead *.cpp map <F8> :! g++ -std=c++11 %:p -o out.exe -g -lboost_system -lboost_thread -pthread -static-libstdc++<CR>:! %:p:h/out.exe<CR>
autocmd BufNewFile,BufRead *.cpp map mkco :! g++ -std=c++11 %:p -o out.exe -O3 -llibgo -lboost_thread -lboost_system -ldl -pthread -static-libstdc++<CR>:! %:p:h/out.exe<CR>
autocmd BufNewFile,BufRead *.cpp map mkcob :! g++ -std=c++11 %:p -o out.exe -O3 -llibgo -lboost_coroutine -lboost_context -lboost_thread -lboost_system -ldl -pthread -static-libstdc++<CR>:! %:p:h/out.exe<CR>

" go
autocmd BufNewFile,BufRead *.go map <F7> :! go build %<CR>
autocmd BufNewFile,BufRead *.go map <F5> :! go run %<CR>

" java
autocmd BufNewFile,BufRead *.java map <F7> :! javac %<CR>
autocmd BufNewFile,BufRead *.java map <F5> <F7>:! java %:r<CR>

"set makeef=compile_error.log
"set makeprg=make.exe
"set shellpipe=

""""""""""""""""""""""""""VimEnv"""""""""""""""""""""""
set path+=/usr/include,/usr/include/linux,/usr/include/c++/4.8,/usr/include/x86_64-linux-gnu,/usr/include/x86_64-linux-gnu/c++/4.8,/usr/include/i386-linux-gnu,/usr/include/i386-linux-gnu/c++/4.8,/usr/local/include

""""""""""""""""""""""""""Style"""""""""""""""""""""""
color evening
filetype on
filetype indent on
filetype plugin on
syntax on
syntax enable
set incsearch
"set ignorecase
set smartcase
set nocompatible
set wildmenu
set number
set hlsearch
set nowrap
set autochdir
set fo-=ro

"折叠
set nofoldenable
set foldmethod=syntax
set foldlevel=1

"tab
set expandtab "Tab转换成空格
set tabstop=4
set shiftwidth=4
set softtabstop=4

set gcr=a:block-blinkon0 "禁止光标闪烁
set guioptions-=m
set guioptions-=T
set laststatus=2
set guifont=Courier\ New:h12
set encoding=utf-8
set fileencoding=utf-8
set fileencodings=utf-8,gbk ",utf-16,gb2312 "可识别文件编码

set cc=80
hi colorcolumn ctermbg=9 guibg=blue

""""""""""""""""""""""""""Plugin Config"""""""""""""""""""""""

" Vundle
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin("~/.vim/bundle")
"Plugin 'https://code.csdn.net/u014579048/vundle-vim.git', {'name': 'Vundle.vim'}
"Plugin 'yyzybb/cppenv'
"Plugin 'yyzybb/quickfixer'
"Plugin 'https://code.csdn.net/u014579048/vim-airline.git'
"Plugin 'https://code.csdn.net/u014579048/nerdtree.git'
"Plugin 'https://code.csdn.net/u014579048/taglist-vim.git', {'name': 'taglist.vim'}
"Plugin 'https://code.csdn.net/u014579048/ultisnips.git'
"Plugin 'https://code.csdn.net/u014579048/vim-snippets.git'
"Plugin 'https://code.csdn.net/u014579048/vim-go.git'
"Plugin 'https://code.csdn.net/u014579048/youcompleteme.git'
Plugin 'gmarik/Vundle.vim'
Plugin 'vim-airline/vim-airline'
Plugin 'scrooloose/nerdtree'
Plugin 'vim-scripts/taglist.vim'
Plugin 'yyzybb/cppenv'
Plugin 'yyzybb/quickfixer'
Plugin 'Valloric/YouCompleteMe'
Plugin 'SirVer/ultisnips'
Plugin 'honza/vim-snippets'
Plugin 'fatih/vim-go'
call vundle#end()
filetype plugin indent on

" YouCompleteMe
let g:ycm_error_symbol = '>>'
let g:ycm_warning_symbol = '>*'
let g:ycm_show_diagnostics_ui = 0
let g:ycm_global_ycm_extra_conf = '~/.ycm_extra_conf.py'
nnoremap gy :YcmCompleter GoToDefinitionElseDeclaration<CR>
nnoremap gu :YcmCompleter GoToImprecise<CR>
nmap <F4> :YcmDiags<CR>
set completeopt=menuone

" UltiSnips
let g:UltiSnipsUsePythonVersion = 2
let g:UltiSnipsExpandTrigger="<c-j>"
let g:UltiSnipsJumpForwardTrigger="<c-j>"
let g:UltiSnipsJumpBackwardTrigger="<c-i>"
let g:UltiSnipsEditSplit="vertical"
let g:UltiSnipsSnippetDirectories=["UltiSnips","cppenv/snippets"]

" airline
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#left_sep = ' '
let g:airline#extensions#tabline#left_alt_sep = '|'

" nerdtree
map <F3> :NERDTreeToggle<CR>

" taglist
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
map TL :Tlist<CR>
map TU :TlistUpdate<CR>

" cppenv
au BufNewFile,BufRead * execute cppenv#dummy()
au BufNewFile,BufRead *.h,*.hpp,*.inl,*.ipp,*.cpp,*.c,*.cc,*.go execute cppenv#infect()
au BufNewFile,BufRead *.h,*.hpp,*.inl,*.ipp,*.cpp,*.c,*.cc,*.go set fo-=ro

" vim-go
let g:go_fmt_autosave = 0
let g:go_def_mapping_enabled = 0
let g:go_bin_path = '/tmp/bin'
"let g:go_highlight_space_tab_error = 0
let g:go_highlight_trailing_whitespace_error = 0
au BufNewFile,BufRead *.go nnoremap gy :GoDef<CR>
au BufNewFile,BufRead *.go nnoremap <F4> :GoErrCheck<CR>

" tags
set tags=tags,./tags,/usr/include/tags
"set tags+=/home/yyz/C/Bex/Bex/tags,/home/yyz/C/Bex/boost/include/tags

" gvim on windows
if !has("unix")
    source $VIMRUNTIME/vimrc_example.vim
    source $VIMRUNTIME/mswin.vim
    behave mswin
endif

set nobackup
set noswapfile
set undofile
set undodir=$VIM/vimfiles/undodir
set undolevels=100
set sel=inclusive
set mouse=a

"SET Comment START
autocmd BufNewFile *.py exec ":call SetComment()" 

func SetComment()
    if expand("%:e") == 'py'
        let line = 1
        call setline(line, '#!/usr/bin/env python')
        call setline(line + 1, '#-*- coding:utf-8 -*-')
        call setline(line + 2, '__metaclass__ = type')
        call setline(line + 3, '#--------------------------------------------------')
        call setline(line + 4, '#')
        call setline(line + 5, '#            Filename: '.expand("%"))
        call setline(line + 6, '#              Author: bailiyang@meizu.com')
        call setline(line + 7, '#              Create: '.strftime("%Y-%m-%d %H:%M:%S"))
        call setline(line + 8, '#       Last Modified: '.strftime("%Y-%m-%d %H:%M:%S"))
        call setline(line + 9, '#')
        call setline(line + 10, '#--------------------------------------------------')
    endif
endfunc
"SET Comment END

"SET Last Modified Time START
func DataInsert()
    call cursor(9, 1)
    if search('Last Modified') != 0
        let line = line('.')
        call setline(line, '#       Last Modified: '.strftime("%Y-%m-%d %H:%M:%S"))
    else
        if search('#!/usr/bin/') != 0
            let line = line('.')
            call setline(line, '#!/usr/bin/env python')
        endif
        if search('coding:utf-8') != 0
            let line = line('.')
            call setline(line, '#-*- coding:utf-8 -*-')
        endif
        if search('__metaclass__ = type') != 0
            let line = line('.')
            call setline(line, '__metaclass__ = type')
        endif
        call append(line, '#--------------------------------------------------')
        call append(line + 1, '#')
        call append(line + 2, '#            Filename: '.expand("%"))
        call append(line + 3, '#              Author: bailiyang@meizu.com')
        call append(line + 4, '#              Create: '.strftime("%Y-%m-%d %H:%M:%S"))
        call append(line + 5, '#       Last Modified: '.strftime("%Y-%m-%d %H:%M:%S"))
        call append(line + 6, '#')
        call append(line + 7, '#--------------------------------------------------')
    endif
endfunc

autocmd FileWritePre,BufWritePre *.py ks| call DataInsert() | 's
"SET Last Modifed Time END
