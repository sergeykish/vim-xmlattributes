import re

class Tag():
    def __init__(self, match, lineno):
        self.text   = match.group(0)
        self.start  = match.start()
        self.end    = match.end()
        self.lineno = lineno

    def body(self):
        return self.text[1:-1]

    def name(self):
        return self.body()

    def test(self, attribute, value):
        return '<%s %s="%s">' % (self.body(), attribute, value)

def scan(line, lineno):
    expression = '<[\w]+?>'
    pattern = re.compile(expression)
    result = [Tag(match, lineno) for match in pattern.finditer(line)]
    if result == []:
        return None
    return result[-1]
