from scanner import scan

def test_return_last():
    assert scan('he<ul><li>one</li><li>two', 0).text, '<li>'

def test_return_open_tags():
    assert scan('he<ul><li>one</li>two', 0).text, '<li>'
