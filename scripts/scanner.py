import re

class Tag():
    def __init__(self, text, start=0, end=0, lineno=0):
        self._text   = text
        self._start  = start
        self._end    = end
        self._lineno = lineno

        self._attributes = {}
        expression = '\s*(?P<attribute>\w+)="(?P<value>.*?)"\s*'
        pattern = re.compile(expression)
        for match in pattern.finditer(self._text):
            self._attributes[match.group('attribute')] = match.group('value')

    def body(self):
        return self._text[1:-1]

    def name(self):
        return self.body().split()[0]

    def test(self, attribute, value):
        return '<%s %s="%s">' % (self.body(), attribute, value)

    def attributes(self):
        return self._attributes.keys()

    def value(self, attribute):
        return self._attributes[attribute] if self._attributes.has_key(attribute) else ''

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_lineno(self):
        return self._lineno

def scan(line, lineno):
    expression = '<[^/].+?>'
    pattern = re.compile(expression)
    result = [Tag(match.group(0), match.start(), match.end(), lineno)
            for match in pattern.finditer(line)]
    if result == []:
        return None
    return result[-1]
