import dfa
from lex import *


def analizer(input1):
    a = []
    b = []

    lexer = Lexer(input1)
    print(input1)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        if(token.kind == TokenType.NUM):
            a.append('NUM')
        if(token.kind == TokenType.ID):
            a.append('ID')
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
    dfa.dfafunction(a)
    return a,b
