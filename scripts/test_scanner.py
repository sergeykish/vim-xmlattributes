from scanner import scan, Tag

def test_return_last():
    assert scan('he<ul><li>one</li><li>two', 0).body() == 'li'

def test_return_open_tags():
    assert scan('he<ul><li>one</li>two', 0).body() == 'li'

def test_attributes_list():
    tag = Tag('<a href="http://google.com" class="varning test">')
    assert tag.attributes() == ['href', 'class']

def test_attribute_value():
    tag = Tag('<a href="http://google.com" class="varning test">')
    assert tag.value('href') == 'http://google.com'
    assert tag.value('class') == 'varning test'
    assert tag.value('id') == ''
