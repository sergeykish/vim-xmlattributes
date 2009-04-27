from scanner import scan, Tag

def test_return_last():
    assert scan('he<ul><li>one</li><li>two', 0).body() == 'li'

def test_return_open_tags():
    assert scan('he<ul><li>one</li>two', 0).body() == 'li'

def test_return_complex():
    assert scan('he<ul><a href="http://google.com" class="varning test">two', 0).body() == \
            'a href="http://google.com" class="varning test"'

def test_name():
    tag = Tag('<a href="http://google.com" class="varning test">')
    assert tag.name() == 'a'

def test_attributes_list():
    tag = Tag('<a href="http://google.com" class="varning test">')
    assert tag.attributes() == ['href', 'class']

def test_attribute_value():
    tag = Tag('<a href="http://google.com" class="varning test">')
    assert tag.get_value('href') == 'http://google.com'
    assert tag.get_value('class') == 'varning test'
    assert tag.get_value('id') == ''

def test_attribute_generation():
    tag = Tag('<a href="http://google.com" class="varning test">')
    assert tag.generate() == '<a href="http://google.com" class="varning test">'
