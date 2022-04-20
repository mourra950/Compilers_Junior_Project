from automata.fa.dfa import DFA
# DFA which matches all binary strings ending in an odd Nber of '1's


def dfafunction(a):
    dfa = DFA(
        states={'start', '1', '2', '3', 'dead'},
        input_symbols={'+', '-', '/', '*', 'ID', 'NUM'},
        transitions={
            'start': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': '1', 'NUM': '2'},
            '1': {'+': '3', '-': '3', '*': '3', '/': '3', 'ID': 'dead', 'NUM': 'dead'},
            '2': {'+': '3', '-': '3', '*': '3', '/': '3', 'ID': 'dead', 'NUM': 'dead'},
            '3': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': '1', 'NUM': '2'},
            'dead': {'+': 'dead', '-': 'dead', '/': 'dead', '*': 'dead', 'ID': 'dead', 'NUM': 'dead'}
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
        print("not valid")

    count = 0
    