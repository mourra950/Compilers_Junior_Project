import dfa
from lex import *


def analizer(input1,condition):
    TOkenTypeList = []
    TOkenTextList = []
    lexer = Lexer(input1)
    print(input1)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
       
        if(token.kind == TokenType.NUM):
            TOkenTypeList.append('N')
        if(token.kind == TokenType.ID):
            TOkenTypeList.append('I')       
        if(token.kind == TokenType.PLUS):
            TOkenTypeList.append('+')
        if(token.kind == TokenType.ASTERISK):
            TOkenTypeList.append('*')
        if(token.kind == TokenType.MINUS):
            TOkenTypeList.append('-')
        if(token.kind == TokenType.DIVIDE):
            TOkenTypeList.append('/')
        TOkenTextList.append(token.text)    
        token = lexer.getToken()
    counter=0
    while(counter<len(TOkenTypeList)-1):
        if(TOkenTypeList[counter]=='N' or TOkenTypeList[counter]=='I'):
            if(TOkenTypeList[counter+1]=='N' or TOkenTypeList[counter+1]== 'I'):
                print(TOkenTypeList[counter+1])
                return 'Invalid','Invalid'
        
        if(TOkenTypeList[counter]=='+' or TOkenTypeList[counter]== '-' or TOkenTypeList[counter]=='/' or TOkenTypeList[counter]== '*'):
            if(TOkenTypeList[counter+1]=='+' or TOkenTypeList[counter+1]== '-' or TOkenTypeList[counter+1]=='/' or TOkenTypeList[counter+1]== '*'):
                return 'Invalid','Invalid'
        counter+=1
    
    
    
    if(condition=="scan"):
        dfa.dfafunction(TOkenTypeList)
    else:
        dfa.dfashow(TOkenTypeList)
        
    
        
        
        
        
        
    return TOkenTypeList,TOkenTextList
#  print((token.kind==TokenType.NUM or TokenType.ID) == (TOkenTypeList[-1]==TokenType.NUM or TokenType.ID))
#         if((token.kind==TokenType.NUM or TokenType.ID) and (TOkenTypeList[-1]==TokenType.NUM or TokenType.ID)):
#             return"Invalid","Invalid"
#         else:

#  if((token.kind==TokenType.PLUS or TokenType.ASTERISK or TokenType.MINUS or TokenType.DIVIDE) and(TOkenTypeList[-1] ==TokenType.PLUS or TokenType.ASTERISK or TokenType.MINUS or TokenType.DIVIDE) ):    
#         return "Invalid","Invalid"
#     else:
   