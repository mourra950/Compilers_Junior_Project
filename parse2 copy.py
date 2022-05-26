from cProfile import label
import sys
from lex import *
import networkx as nx
import teenytiny as t
import networkx as nx
from matplotlib import pyplot as plt

# Parser object keeps track of current token and checks if the code matches the grammar.


class Parser:
    def __init__(self, lexer):
        self.lis=list('(')
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
            
            self.expressionTemp()
    # One of the following statements...

    def expressionTemp(self):
        temp=self.counter
        
        self.lis.append('Expression')
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
        # print(self.counter,'add op 7')
        self.counter+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 8')
        self.counter+=1
        self.lis.append('addop')
        print('Addop: ')
        if self.checkToken(TokenType.MINUS):
            self.lis.append('-')
            print("-")
            self.nextToken()
        elif self.checkToken(TokenType.PLUS):
            self.lis.append('+')
            print("+")
            self.nextToken()
        

    def expressionDash(self):
        temp=self.counter
        
        print('Expressiondash')
        self.lis.append('Expressiondash')
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
            self.lis.append('ε')
            print("ε")
            self.counter+=1


    def term(self):
        temp=self.counter #1
        
        print("Term ")
        self.lis.append('Term')
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
        self.lis.append('termdash')
        self.counter+=1
        if self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.DIVIDE):
            
            self.G.add_edge(str(temp),str(temp+1))
           
            self.Mulop()
            
            self.G.add_edge(str(temp),str(self.counter))
            
            self.factor()
            # print(self.counter)
            self.G.add_edge(str(temp),str(self.counter))
            self.termDash()
            # print('pokemon')
            # print(self.counter)
            
            # Simple string.
        else:
            self.G.add_edge(str(temp),self.counter)
            print("ε")
            self.lis.append('ε')
            self.counter+=1

    def factor(self):
        print('factor')
        self.lis.append('factor')
        self.G.add_edge(str(self.counter),str(self.counter+1))
        self.counter+=2 #4
        if self.checkToken(TokenType.NUM):
            
            self.lis.append('number')
            print("number")
            self.nextToken()
        elif self.checkToken(TokenType.ID):
            print("identifier")
            self.lis.append('identifier')
            self.nextToken()
        elif self.checkToken(TokenType.OPENBRACKET):
            print(TokenType.OPENBRACKET)
            self.nextToken()
            self.expressionTemp()
            print(TokenType.CLOSEDBRACKET)
            self.nextToken()

    def Mulop(self):
        
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 8')
        self.counter+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 9')
        self.counter+=1
        print('Mulop')
        self.lis.append('mulop')
        if self.checkToken(TokenType.DIVIDE):
            self.lis.append('/')
            print("/")
            self.nextToken()
        elif self.checkToken(TokenType.ASTERISK):
            print("*")
            self.lis.append('*')
            self.nextToken()


def main():
    g=nx.Graph()
    lex , txt,token=t.analizer('3','scan')
    lex = list(lex)
    print("//////////////////////////////////////////////////////////////////////////////////////////////")
    P = Parser(token)
    P.program()
    terminals=['ε','number','+','-','*','/','identifier']
    nonterminals=['Term','factor','termdash','Expression','Expressiondash','addop','mulop']
    print('#########################################')
    buff=''
    tc = 0
    j = 0
    for i in P.lis:
        if i in nonterminals:
            buff+=str(' ( ')
            buff+=str( i )
            tc+=1
        elif i in terminals:
            buff += str(' ')
            buff+=str(i)
            buff+=str(' ) ')
            j+=2
    print(tc,j)
    print(buff)
main()

