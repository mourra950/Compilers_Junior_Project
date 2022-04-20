import dfa
from lex import *


def analizer(input1,condition):
    a = []
    b = []

    lexer = Lexer(input1)
    print(input1)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        if(token.kind == TokenType.NUM):
            a.append('N')
        if(token.kind == TokenType.ID):
            a.append('I')
        if(token.kind == TokenType.PLUS):
            a.append('+')
        if(token.kind == TokenType.ASTERISK):
            a.append('*')
        if(token.kind == TokenType.MINUS):
            a.append('-')
        if(token.kind == TokenType.DIVIDE):
            a.append('/')
        b.append(token.text)    
        token = lexer.getToken()
    if(condition=="scan"):
        dfa.dfafunction(a)
    else:
        dfa.dfashow(a)
    return a,b
