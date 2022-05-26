#root of the syntax tree
import teenytiny as teeny
def syntaxtree(input):
    treel=[]
    listemp=[]
    lis=['N','+','N','-','N','*','N','+','N'] #n+n-r*t
    text,lex,t=teeny.analizer(input,'scan')
    print(text,lex,t)
    lis=list(text)
    if ['(',')'] in lis:
        pass
    else:
        while len(lis)!=1:
            index=0
            operator=0
            
            
            while index<len(lis):
                
                if lis[index]=='*':
                    listemp.append(lis.copy())
                    treel.append('Multy'+str(operator)+' connected to '+lis[index+1]+ ' and '+lis[index-1])
                    lis[index]='Multy'+str(operator)
                    operator+=1
                    lis.pop(index+1)
                    lis.pop(index-1)
                    index=0
                if lis[index]=='/':
                    treel.append('Div'+str(operator)+' connected to '+lis[index+1]+ ' and '+lis[index-1])
                    lis[index]='Div'+str(operator)
                    operator+=1
                    lis.pop(index+1)
                    lis.pop(index-1)
                    index=0
                index+=1
            index=0
            while index<len(lis):
                if lis[index]=='+':
                    treel.append('Plus'+str(operator)+' connected to '+lis[index+1]+ ' and '+lis[index-1])
                    lis[index]='Plus'+str(operator)
                    listemp.append(lis.copy())
                    lis[index]='Plus'+str(operator)
                    operator+=1
                    lis.pop(index+1)
                    lis.pop(index-1)
                    index =0
                elif lis[index]=='-':
                    listemp.append(lis.copy())
                    treel.append('Minus'+str(operator)+' connected to '+lis[index+1]+ ' and '+lis[index-1])
                    lis[index]='Minus'+str(operator)
                    operator+=1
                    lis.pop(index+1)
                    lis.pop(index-1)
                    index =0
                index+=1
            listemp.append(lis.copy())
        
        for i in treel:
            print(i)