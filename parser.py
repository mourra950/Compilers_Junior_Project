import sys
from lex import *

# Parser object keeps track of current token and checks if the code matches the grammar.
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer

        self.symbols = set()    # All variables we have declared so far.
        self.labelsDeclared = set() # Keep track of all labels declared
        self.labelsGotoed = set() # All labels goto'ed, so we know if they exist or not.

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
            self.abort("Expected " + kind.name + ", got " + self.curToken.kind.name)
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
        # Parse all the expressions in the program.
        while not self.checkToken(TokenType.EOF):
            print('expression')
            self.expressionTemp()         
    # One of the following statements...
    def expressionTemp(self):
        self.term()
        self.expressionDash()
        self.nextToken()  
    def Addop(self):
        if self.checkToken(TokenType.MINUS):
            print("MINUS")
            self.nextToken()
        elif self.checkToken(TokenType.PLUS):
            print("PLUS")
            self.nextToken()
    def expressionDash(self):
        if self.checkToken(TokenType.MINUS) or self.checkToken(TokenType.PLUS):
            self.Addop()
            self.term()
            self.expressionDash()
            self.nextToken()
        else:
            print("Epsilon")
            self.nextToken()
            
    def term (self):
        self.factor()
        self.termDash()
        self.nextToken()
          
    def termDash(self):
        if self.checkToken(TokenType.ASTERISK) or self.checkToken(TokenType.DIVIDE):
                self.mulop()
                self.factor()
                self.termDash()
                self.nextToken()
                # Simple string.
        else :
            print("Epsilon")
            self.nextToken() 
    def factor(self):
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
         if self.checkToken(TokenType.DIVIDE):
             print("/")
             self.nextToken()
         elif self.checkToken(TokenType.ASTERISK):
             print("*")   
             self.nextToken()

             
            
                
   