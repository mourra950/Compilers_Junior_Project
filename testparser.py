import teenytiny as t

from lex import *
from parse import *
def main():
    lex , txt,token=t.analizer('5+4','scan')
    print("//////////////////////////////////////////////////////////////////////////////////////////////")
    P = Parser(token)
    P.program()
    
main()