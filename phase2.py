import nltk as nltk

 
groucho_grammar = nltk.CFG.fromstring("""
exp -> term E
E -> addop term E | 'Eps'
addop -> '+' | '-'
term -> factor T
T -> mullop factor T | 'Eps'
mullop -> '*' | '/'
factor -> '(' exp ')' | 'Identifier' | 'Number'

 """)
# groucho_grammar = nltk.CFG.fromstring("""
# exp -> exp addop term | term
# addop -> '+' | '-'
# term -> term mullop factor |factor
# mullop -> '*' | '/'
# factor -> '(' exp ')' | 'Identifier' | 'Number'
#  """)

# >>> groucho_grammar = nltk.CFG.fromstring("""
# ... S -> NP VP
# ... PP -> P NP
# ... NP -> Det N | Det N PP | 'I'
# ... VP -> V NP | VP PP
# ... Det -> 'an' | 'my'
# ... N -> 'elephant' | 'pajamas'
# ... V -> 'shot'
# ... P -> 'in'
# ... """)

def main():
    global groucho_grammar
    sent=['Number','-','Number','-','Number','+','Number']
    parser = nltk.ChartParser(groucho_grammar)
    
    for tree in parser.parse(sent):
        print('omar')
        print(tree)
    
main()    