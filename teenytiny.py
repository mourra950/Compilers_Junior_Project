import dfa
from lex import *


def main(input1):
    a = []
    
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
        token = lexer.getToken()
    print(a)
    dfa.dfafunction(a)
   


