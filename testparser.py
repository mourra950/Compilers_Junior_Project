import teenytiny as t
import dfa
from lex import *
def main():
    lex , txt=t.analizer('5+4','p')
    print(lex)
main()