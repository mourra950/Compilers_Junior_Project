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
        self.counter = 0
        self.countert = 0
        self.Gt = nx.DiGraph()
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
        temp=self.countert
        print('Expression')
        self.G.add_edge(str(temp),str(temp+1))
        self.counter +=1
        self.term()
        self.counter+=1
        self.G.add_edge(str(temp),str(self.counter))
<<<<<<< Updated upstream
        
        self.expressionDash()
=======
        #print('mmaaaaaaaaaaaaaamaa')
        print(self.curToken.kind)
        self.expressionDash()
        #print('mmaaaaaaaaaaaaaamaa')
>>>>>>> Stashed changes
        self.nextToken()

    def Addop(self):
        self.Gt.add_edge(str(self.countert),str(self.countert+1))
        self.countert+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 7')
        self.counter+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 8')
        self.counter+=1
        print('Addop: ', end=' ')
        if self.checkToken(TokenType.MINUS):
            print("-")
            self.nextToken()
        elif self.checkToken(TokenType.PLUS):
            print("+")
            self.nextToken()
<<<<<<< Updated upstream
        

=======
       
>>>>>>> Stashed changes
    def expressionDash(self):
        temp=self.counter
        
        print('Expressiondash')
        self.counter+=1
        if self.checkToken(TokenType.MINUS) or self.checkToken(TokenType.PLUS):
            print("Aywa")
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
            print("ε")
            self.counter+=1
<<<<<<< Updated upstream


=======
            self.nextToken()
       
>>>>>>> Stashed changes
    def term(self):
        temp=self.counter #1
        
        print("Term ")
        
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
<<<<<<< Updated upstream
            self.counter+=1
=======
            self.nextToken()    
>>>>>>> Stashed changes

    def factor(self):
        print('factor')
        self.G.add_edge(str(self.counter),str(self.counter+1))
        self.counter+=2 #4
        if self.checkToken(TokenType.NUM):
            self.Gt.add_edge(self.countert,self.countert+1)
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
        self.Gt.add_edge(str(self.countert),str(self.countert+1))
        self.countert+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 8')
        self.counter+=1
        self.G.add_edge(str(self.counter-1),str(self.counter))
        # print(self.counter,'add op 9')
        self.counter+=1
        print('Mulop')
        if self.checkToken(TokenType.DIVIDE):
            print("/")
            self.nextToken()
        elif self.checkToken(TokenType.ASTERISK):
            print("*")
            self.nextToken()
           


def main():
    g=nx.Graph()
    lex , txt,token=t.analizer('3','scan')
    lex=list(lex)
    index=1
    
    g.add_edge(index,index+1)
    g.add_edge(index+1,index+2)
    
    print("//////////////////////////////////////////////////////////////////////////////////////////////")
    P = Parser(token)
    P.program()
    nx.draw_shell(g,with_labels = True,node_size=100)
    plt.show()
main()


