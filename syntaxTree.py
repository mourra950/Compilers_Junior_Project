#root of the syntax tree
listemp=[]
lis=['N','+','N','-','N','*','N','+','N'] #n+n-r*t
while len(lis)!=1:
    index=0
    
    while index<len(lis):
        
        if lis[index]=='*':
            listemp.append(lis.copy())
            lis[index]='Multy'
            lis.pop(index+1)
            lis.pop(index-1)
        index+=1
    index=0
    while index<len(lis):
        
        if lis[index]=='/':
            listemp.append(lis.copy())
            lis[index]='Div'
            lis.pop(index+1)
            lis.pop(index-1)
        index+=1
    index=0
    while index<len(lis):
        
        if lis[index]=='+':
            listemp.append(lis.copy())
            lis[index]='Plus'
            lis.pop(index+1)
            lis.pop(index-1)
        index+=1
    index=0
    while index<len(lis):
        
        if lis[index]=='-':
            listemp.append(lis.copy())
            lis[index]='Minus'
            lis.pop(index+1)
            lis.pop(index-1)
        index+=1
for i in listemp:
    print(i)