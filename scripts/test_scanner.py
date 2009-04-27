from scanner import scan, Tag

def test_return_last():
    assert scan('he<ul><li>one</li><li>two', 0).body() == 'li'

def test_return_open_tags():
    assert scan('he<ul><li>one</li>two', 0).body() == 'li'

def test_return_complex():
    assert scan('he<ul><a href="http://google.com" class="varning test">two', 0).body() == \
            'a href="http://google.com" class="varning test"'

class TestTag:
    def setUp(self):
        self._tag = Tag('<a href="http://google.com" class="varning test">')

    def test_name(self):
        assert self._tag.name() == 'a'

    def test_list(self):
        assert self._tag.attributes() == ['href', 'class']

    def test_value(self):
        assert self._tag.get_value('href') == 'http://google.com'
        assert self._tag.get_value('class') == 'varning test'
        assert self._tag.get_value('id') == ''

    def test_generation(self):
        assert self._tag.generate() == '<a href="http://google.com" class="varning test">'

    def test_delete(self):
        self._tag.set_value('class', '')
        assert self._tag.generate() == '<a href="http://google.com">'
