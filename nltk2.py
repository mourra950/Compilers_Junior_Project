import nltk as nltk
import nltk.draw as draw 
def main():
    txt='( Expression ( Term ( factor number )  ( termdash ε )  ( Expressiondash ( addop + )  ( Term ( factornumber)  ( termdash ( mulop * )  ( factor number )  ( termdash ε )  ( Expressiondash ( addop - )  ( Term ( factor number )  ( termdash ε )  ( Expressiondash ε) )))))))'
    tree=nltk.Tree.fromstring(txt)
    draw.draw_trees(tree)
    
main()