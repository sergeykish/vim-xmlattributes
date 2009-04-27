import vim
import os, sys
sys.path.append(os.path.expanduser("~/.vim/scripts/"))

from scanner import scan

class Shortcuted:
    def __init__(self, symbol, f):
        self._symbol = symbol
        self._f = f

    def _map(self):
        vim.command("cnoremap %s <CR>" % self._symbol)

    def _unmap(self):
        vim.command("silent! cunmap %s" % self._symbol)

    def __call__(self, *fargs, **kw):
        self._map()
        try:
            ret = self._f(*fargs, **kw)
        except (Exception, KeyboardInterrupt):
            self._unmap()
        return ret

def vim_input(message='input : ', default=''):
    vim.command("call inputsave()")
    vim.command("let user_input = input('%s','%s')" % (message, default))
    vim.command("call inputrestore()")
    value = vim.eval('user_input')
    if value is None:
        raise Exception
    return value

def input_attribute(name, attributes):
    # Completion from list
    return Shortcuted('=', vim_input)('<%s ' % name)

def input_value(name, attribute, default=''):
    return Shortcuted('"', vim_input)('<%s %s="' % (name, attribute), default)

def vim_replace(lineno, start, end, str):
    cb = vim.current.buffer
    line = cb[lineno]
    cb[lineno] = line[:start] + str + line[end:]

def attribute(method):
    try:
        tag = get_latest_tag()
        if tag is None:
            return

        attribute = input_attribute(tag.name(), tag.attributes())
        if method == 'd':
            tag.set_value(attribute, '')
        else:
            default = tag.get_value(attribute) if method == 'y' else ''
            value = input_value(tag.name(), attribute, default)
            tag.set_value(attribute, value)
        vim_replace(tag.get_lineno(), tag.get_start(), tag.get_end(), tag.generate())
        print tag.generate()
    except:
        pass

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
