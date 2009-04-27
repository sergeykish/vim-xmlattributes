import vim
import os, sys
sys.path.append(os.path.expanduser("~/.vim/scripts/"))

from scanner import scan

def attribute(method):
    tag = get_latest_tag()
    if tag is None:
        return
    print tag.test()

    # replace
    cb = vim.current.buffer
    line = cb[tag.line]
    cb[tag.line] = line[:tag.start] + tag.test() + line[tag.end:]

def is_current(line):
    cl, dummy = vim.current.window.cursor
    return line == cl - 1

# There are many places for cursor, it is marked "{}"
# <{}div ...>...</div>
# <div ...>...{}...</div>
# <div ...>...</div{}>
def get_latest_tag():
    cl, cc = vim.current.window.cursor
    cb = vim.current.buffer
    # doesn't want </tag>
    for lineno in reversed(xrange(cl)):
        line = cb[lineno]
        # first line begins from current col
        if is_current(lineno):
            line = line[0:cc + 1]
        result = scan(line, lineno)
        if not result is None:
            return result
    return None
