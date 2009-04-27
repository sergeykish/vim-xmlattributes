pyfile ~/.vim/scripts/xmlattributes.py

nnoremap <silent> <Plug>DAttribute :<C-U>python attribute("d")<CR>
nnoremap <silent> <Plug>YAttribute :<C-U>python attribute("y")<CR>

nmap dattr <Plug>DAttribute
nmap yattr <Plug>YAttribute

