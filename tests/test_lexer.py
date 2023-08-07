import fat

def test_lexer():
    lex = fat.Lexer([1,2,3])
    assert len(lex) == 3
    assert lex[0] == 1
    assert lex[1] == 2
    assert lex[2] == 3
    assert lex[3] == None
    assert lex[4] == None

    assert lex.read() == 1
    assert lex.read() == 2
    assert lex.read() == 3
    assert lex.read() == None
    assert lex.read() == None

    assert len(lex) == 0
    assert lex[0] == None

    lex.move(-1)
    assert lex[0] == 3
    assert lex[1] == None

    lex.move(-1)
    assert lex[0] == 2
    assert lex[1] == 3

    lex.move(-1)
    assert lex[0] == 1

    lex.move(-1)
    assert lex[0] == 1
