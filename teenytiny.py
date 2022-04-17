import dfa
from lex import *


def main():
    a = []
    input1 = input("enter the lexical expression to analyze : ")
    lexer = Lexer(input1)

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
    dfa.dfafunction(a)


main()
