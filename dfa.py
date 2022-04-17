from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an odd Nber of '1's
dfa = DFA(
    states={'start', '1', '2', '3', '4', '5', '6', 'dead'},
    input_symbols={'+', '-', '/', '*', 'I', 'N'},
    transitions={
        'start': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': '1', 'N': '2'},
        '1': {'+': '3', '-': '4', '*': '5', '/': '6', 'I': 'dead', 'N': 'dead'},
        '2': {'+': '3', '-': '4', '*': '5', '/': '6', 'I': 'dead', 'N': 'dead'},
        '3': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': '1', 'N': '2'},
        '4': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': '1', 'N': '2'},
        '5': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': '1', 'N': '2'},
        '6': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': '1', 'N': '2'},
        'dead': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'I': 'dead', 'N': 'dead'}
    },
    initial_state='start',
    final_states={'1', '2'}
)

print(dfa.read_input('I+I+N/I-N'))
