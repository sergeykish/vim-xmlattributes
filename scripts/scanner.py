import re

class Tag():
    def __init__(self, match, line):
        self.name  = match.group(0)
        self.start = match.start()
        self.end   = match.end()
        self.line  = line

    def body(self):
        return self.name[1:-1]

    def test(self):
        return '<%s class="test">' % self.body()

def scan(line, lineno):
    expression = '<[\w]+?>'
    pattern = re.compile(expression)
    result = [Tag(match, lineno) for match in pattern.finditer(line)]
    if result == []:
        return None
    return result[-1]
