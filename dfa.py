from automata.fa.dfa import DFA
from pandas import*
from graphviz import Digraph
from jupyterlab import*
from colormath import *
import pydot
from matplotlib.pyplot import show
from graphviz import Digraph
from visual_automata.fa.dfa import VisualDFA
# DFA which matches all binary strings ending in an odd Nber of '1's


def dfafunction(a):
    dfa = DFA(
        states={'start', '1', '2', '3', 'dead'},
        input_symbols={'+', '-', '/', '*', 'I', 'N'},
        transitions={
            'start': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': '1', 'N': '2'},
            '1': {'+': '3', '-': '3', '*': '3', '/': '3', 'I': 'dead', 'N': 'dead'},
            '2': {'+': '3', '-': '3', '*': '3', '/': '3', 'I': 'dead', 'N': 'dead'},
            '3': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': '1', 'N': '2'},
            'dead': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': 'dead', 'N': 'dead'}
        },
        initial_state='start',
        final_states={'1', '2'}
    )
    b = []
    
    if dfa.accepts_input(a):
        print("final state is :"+str(dfa.read_input(a)))
    else:
        print("the last visited state is not accepted")

    try:
        b = dfa.read_input_stepwise(a)
    except:
        print("not valI")

    count = 0
    dfa = VisualDFA(dfa)
    test=""
    for i in a:
        test+=i
       
    dfa.show_diagram(test,filename='DFAA',view=True,state_seperation=3)
    
   



b=['N','+','I','+','+']
dfafunction(b)