import nltk as nltk
import nltk.draw as draw


def drawparsingtree(txt):
    # txt = '( ( Expression ( ( Term ( factor number ) ( termdash ( mulop * ) ( factor number ) ( termdash ε ) ) ) ( Expressiondash ( addop - ) ( Term ( factor number ) ( termdash ε ) ) ( Expressiondash ε ) ))))'
    tree = nltk.Tree.fromstring(txt)
    draw.draw_trees(tree)



