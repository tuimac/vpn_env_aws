colorscheme koehler
syntax on
filetype on
filetype plugin on
filetype indent on
syntax enable
nnoremap <Esc><Esc> :nohlsearch<CR><ESC>
set nocompatible
set backspace=indent,eol,start
set clipboard=unnamed,autoselect
set number
set listchars=tab:^\ ,trail:~
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
set autoindent
set ruler
set ttimeoutlen=10
set hlsearch
set ignorecase
set smartcase
set wildmenu
set noswapfile
set backup
set backupdir=/etc/vim/backup
set undofile
set undodir=/etc/vim/undo
set encoding=utf-8
set statusline=%#LineNr#
set statusline+=%F
set statusline+=%#Cursor#
set statusline+=\ %m
set statusline+=%=
set statusline+=%#CursorColumn#
set statusline+=\ %{&fileencoding?&fileencoding:&encoding}
set statusline+=\[%{&fileformat}\]
set statusline+=\ %p%%
set statusline+=\ %l:%c
set laststatus=2

if has("autocmd")
    autocmd BufNewFile,BufRead *.sh setfiletype bash

    autocmd FileType c          setlocal sw=4 sts=4 ts=4 et
    autocmd FileType html       setlocal sw=2 sts=2 ts=2 et
    autocmd FileType ruby       setlocal sw=4 sts=4 ts=4 et
    autocmd FileType js         setlocal sw=4 sts=4 ts=4 et
    autocmd FileType zsh        setlocal sw=4 sts=4 ts=4 et
    autocmd FileType python     setlocal sw=4 sts=4 ts=4 et
    autocmd FileType scala      setlocal sw=4 sts=4 ts=4 et
    autocmd FileType json       setlocal sw=4 sts=4 ts=4 et
    autocmd FileType css        setlocal sw=4 sts=4 ts=4 et
    autocmd FileType scss       setlocal sw=4 sts=4 ts=4 et
    autocmd FileType sass       setlocal sw=4 sts=4 ts=4 et
    autocmd FileType javascript setlocal sw=4 sts=4 ts=4 et
    autocmd FileType yaml       setlocal sw=2 sts=2 ts=2 et
    autocmd FileType python     setlocal sw=4 sts=4 ts=4 et
    autocmd FileType bash       setlocal sw=4 sts=4 ts=4 et
    au filetype html        set omnifunc=htmlcomplete#CompleteTags
    au filetype xml         set omnifunc=xmlcomplete#CompleteTags
endif
