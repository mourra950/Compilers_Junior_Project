from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an odd Nber of '1's
dfa = DFA(
    states={'start', '1', '2', '3', '4', '5', '6', 'dead'},
    input_symbols={'+', '-', '/', '*', 'ID', 'NUM'},
    transitions={
        'start': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': '1', 'NUM': '2'},
        '1': {'+': '3', '-': '4', '*': '5', '/': '6', 'ID': 'dead', 'NUM': 'dead'},
        '2': {'+': '3', '-': '4', '*': '5', '/': '6', 'ID': 'dead', 'NUM': 'dead'},
        '3': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': '1', 'NUM': '2'},
        '4': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': '1', 'NUM': '2'},
        '5': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': '1', 'NUM': '2'},
        '6': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': '1', 'NUM': '2'},
        'dead': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': 'dead', 'NUM': 'dead'}
    },
    initial_state='start',
    final_states={'1', '2'}
)
a = ['ID', '+', 'NUM']
print("final state is :"+str(dfa.read_input(a)))
b = dfa.read_input_stepwise(a)
count = 0
for i in b:
    print("step: "+str(count)+" is state "+str(i))
    count += 1
# lalalalala
