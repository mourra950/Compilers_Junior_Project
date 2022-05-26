from email import parser
import nltk2 as PnDraw
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
            self.lis.append('(')
            self.expressionTemp()
    # One of the following statements...

    def expressionTemp(self):
        self.lis.append('Expression')
        self.lis.append('(')
        print('Expression')        
        self.term()
        
        self.expressionDash()
        
        
        
        

    def Addop(self):
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 7')
        self.counter+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 8')
        self.counter+=1
        self.lis.append('(')
        self.lis.append('addop')
        print('Addop: ')
        if self.checkToken(TokenType.MINUS):
            self.lis.append('-')
            print("-")
            self.lis.append(')')
            self.nextToken()
        elif self.checkToken(TokenType.PLUS):
            self.lis.append('+')
            self.lis.append(')')
            print("+")
            self.nextToken()
        

    def expressionDash(self):
        temp=self.counter
        
        print('Expressiondash')
        self.lis.append('(')
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
            self.lis.append(')')
        else:
            self.G.add_edge(str(temp),str(temp+1))
            self.lis.append('ε')
            self.lis.append(')')
            print("ε")
            self.counter+=1


    def term(self):
        
        
        print("Term ")
        self.lis.append('(')
        self.lis.append('Term')
        
     
        self.factor()
        #/////////////
        
        
        self.termDash()
        self.lis.append(')')
        # self.nextToken()

    def termDash(self):
        temp=self.counter #4
        print("termdash")
        self.lis.append('(')
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
            self.lis.append(')')
            # print('pokemon')
            # print(self.counter)
            
            # Simple string.
        else:
            self.G.add_edge(str(temp),self.counter)
            print("ε")
            self.lis.append('ε')
            self.lis.append(')')
            self.counter+=1

    def factor(self):
        print('factor')
        
        self.lis.append('(')
        self.lis.append('factor')
        
        if self.checkToken(TokenType.NUM):
            
            self.lis.append('number')
            print("number")
            self.lis.append(')')
            self.nextToken()
        elif self.checkToken(TokenType.ID):
            print("identifier")
            self.lis.append('identifier')
            self.lis.append(')')
            self.nextToken()
        elif self.checkToken(TokenType.OPENBRACKET):
            print('(')
            self.lis.append('OB')
            print(self.curToken.kind)
            self.nextToken()
            
            self.expressionTemp()
            
            self.nextToken()
            self.lis.append('CL')
            print(')')
            self.nextToken()
            
        elif self.checkToken(TokenType.CLOSEDBRACKET):
            
            print(')')
            self.nextToken()

    def Mulop(self):
        
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 8')
        self.counter+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 9')
        self.counter+=1
        print('Mulop')
        self.lis.append('(')
        self.lis.append('mulop')
        if self.checkToken(TokenType.DIVIDE):
            self.lis.append('/')
            print("/")
            self.lis.append(')')
            self.nextToken()
        elif self.checkToken(TokenType.ASTERISK):
            print("*")
            self.lis.append('*')
            self.lis.append(')')
            self.nextToken()


def parserTree(input):
    g=nx.Graph()
    lex , txt,token=t.analizer(input,'scan')
    lext = list(txt)
    print(lext)
    print("//////////////////////////////////////////////////////////////////////////////////////////////")
    P = Parser(token)
    P.program()
    terminals=['number','identifier','ε','+','-','/','*']
    nonterminals=['Term','termdash','Expression','Expressiondash','addop']
    print('#########################################')
    buff='('
    index=0
    # for i in P.lis:
    #     if i in terminals:
    #         if (i=='ε'):
    #             continue
    #         else:
    #             print(i)
                
    #         buff+=str(i)+' '
    #         buff+=  ')'+' '
    #         if i =='ε':
    #             buff+=')'+' '
    #     if i in nonterminals:
    #         buff+='('+' '
    #         buff+=str(i)+' '
    # print('#########################3')
                
        # if i in nonterminals:
        #     print('(')
        #     buff+=str('(')
        # if i in terminals:
        #     buff+=str(')')
    txt=' '.join(P.lis)+')))'
    print(txt)
    PnDraw.drawparsingtree(txt)
    
    
parserTree('3+3')


