import sys

from sympy import root
from lex import *
import networkx as nx
import teenytiny as t
import networkx as nx
from matplotlib import pyplot as plt


# Parser object keeps track of current token and checks if the code matches the grammar.
g=nx.Graph()

class Parser:
    def __init__(self, lexer):
        self.counter = 0
        self.lexer = lexer
        self.G = nx.DiGraph()
        self.symbols = set()    # All variables we have declared so far.
        self.labelsDeclared = set()  # Keep track of all labels declared
        # All labels goto'ed, so we know if they exist or not.
        self.labelsGotoed = set()

        self.curToken = None
        self.peekToken = None
        self.nextToken()
        self.nextToken()    # Call this twice to initialize current and peek.

    # Return true if the current token matches.
    def checkToken(self, kind):
        return kind == self.curToken.kind

    # Return true if the next token matches.
    def checkPeek(self, kind):
        return kind == self.peekToken.kind

    # Try to match current token. If not, error. Advances the current token.
    def match(self, kind):
        if not self.checkToken(kind):
            self.abort("Expected " + kind.name +
                       ", got " + self.curToken.kind.name)
        self.nextToken()

    # Advances the current token.
    def nextToken(self):
        self.curToken = self.peekToken
        self.peekToken = self.lexer.getToken()
        # No need to worry about passing the EOF, lexer handles that.

    # Return true if the current token is a comparison operator.
    def isComparisonOperator(self):
        return self.checkToken(TokenType.GT) or self.checkToken(TokenType.GTEQ) or self.checkToken(TokenType.LT) or self.checkToken(TokenType.LTEQ) or self.checkToken(TokenType.EQEQ) or self.checkToken(TokenType.NOTEQ)

    def abort(self, message):
        sys.exit("Error. " + message)

    # Production rules.

    # program ::= {statement}

    def program(self):
        print("Start")
        self.G.add_edge(str('start'),str(self.counter))
        # Parse all the expressions in the program.
        while not self.checkToken(TokenType.EOF):
            print('ana hena')
            self.expressionTemp()
    # One of the following statements...

    def expressionTemp(self):
        temp=self.counter
        print('Expression')
        self.G.add_edge(str(temp),str(temp+1))
        self.counter +=1
        self.term()
        self.counter+=1
        self.G.add_edge(str(temp),str(self.counter))
        
        self.expressionDash()
        self.nextToken()

    def Addop(self):
        self.G.add_edge(str(self.counter-1),str(self.counter))
        print(self.counter,'add op 7')
        self.counter+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        print(self.counter,'add op 8')
        self.counter+=1
        print('Addop: ', end=' ')
        if self.checkToken(TokenType.MINUS):
            print("-")
            self.nextToken()
        elif self.checkToken(TokenType.PLUS):
            print("+")
            self.nextToken()

    def expressionDash(self):
        temp=self.counter
        
        print('Expressiondash')
        self.counter+=1
        if self.checkToken(TokenType.MINUS) or self.checkToken(TokenType.PLUS):
            self.G.add_edge(str(temp),str(temp+1))
            self.Addop()
            self.G.add_edge(str(temp),str(self.counter))
            self.term()
            self.G.add_edge(str(temp),str(self.counter+1))
            self.counter+=1
            self.expressionDash()
            self.nextToken()
        else:
            self.G.add_edge(str(temp),str(temp+1))
            print("??")
            self.counter+=1
            self.nextToken()

    def term(self):
        temp=self.counter #1
        
        print("term ")
        
        self.G.add_edge(str(temp),str(temp+1))
        self.counter+=1 #2
        self.factor()
        #/////////////
        self.G.add_edge(str(temp),str(self.counter))
        
        self.termDash()
        # self.nextToken()

    def termDash(self):
        temp=self.counter #4
        print("termdash")
        self.counter+=1
        if self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.DIVIDE):
            self.mulop()
            self.factor()
            self.termDash()
            self.nextToken()
            # Simple string.
        else:
            self.G.add_edge(str(temp),self.counter)
            print("??")

    def factor(self):
        print('factor')
        self.G.add_edge(str(self.counter),str(self.counter+1))
        self.counter+=2 #4
        if self.checkToken(TokenType.NUM):
            print("number")
            self.nextToken()
        elif self.checkToken(TokenType.ID):
            print("identifier")
            self.nextToken()
        elif self.checkToken(TokenType.OPENBRACKET):
            print(TokenType.OPENBRACKET)
            self.nextToken()
            self.expressionTemp()
            print(TokenType.CLOSEDBRACKET)
            self.nextToken()

    def Mulop(self):
        
        print('Mulop')
        if self.checkToken(TokenType.DIVIDE):
            print("/")
            self.nextToken()
        elif self.checkToken(TokenType.ASTERISK):
            print("*")
            self.nextToken()

    def syntaxTree(self):
        global counter
        temp=[]
        temp=self.counter 
        if self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.DIVIDE) or self.checkToken(TokenType.PLUS) or self.checkToken(TokenType.MINUS):
            g.add_node()
            
def main():
    lex , txt,token=t.analizer('3-5','scan')
    print("//////////////////////////////////////////////////////////////////////////////////////////////")
    P = Parser(token)
    P.program()
    nx.draw_shell(P.G,with_labels = True,node_size=100)
    plt.show()
main()