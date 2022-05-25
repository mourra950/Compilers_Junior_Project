import teenytiny as t
import networkx as nx
from matplotlib import pyplot as plt

from lex import *
from parse import *
def main():
    lex , txt,token=t.analizer('5+4','scan')
    print("//////////////////////////////////////////////////////////////////////////////////////////////")
    P = Parser(token)
    P.program()
    nx.draw(nx.topological_sort(P.G),with_labels = True,node_size=100)
    plt.show()
main()