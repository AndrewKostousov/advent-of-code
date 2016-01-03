circuit = {}
circuit_evaluated = {}


def primitive_eval(arg):
    if arg.isdigit():
        return int(arg)
    else:
        if arg in circuit_evaluated:
            return circuit_evaluated[arg]
        value = eval_signal_for(arg)
        circuit_evaluated[arg] = value
        return value


def eval_signal_for(target):
    # print target
    assert not target.isdigit(), 'invalid target: ' + target
    # print circuit[target]
    op = circuit[target][0]
    arg1 = circuit[target][1]
    if op == 'copy':
        return primitive_eval(arg1)
    elif op == 'not':
        return ~primitive_eval(arg1)
    elif op == 'and':
        arg2 = circuit[target][2]
        return primitive_eval(arg1) & primitive_eval(arg2)
    elif op == 'or':
        arg2 = circuit[target][2]
        return primitive_eval(arg1) | primitive_eval(arg2)
    elif op == 'lshift':
        arg2 = circuit[target][2]
        return primitive_eval(arg1) << arg2
    elif op == 'rshift':
        arg2 = circuit[target][2]
        return primitive_eval(arg1) >> arg2


for line in open('07.in').read().splitlines():
    parts = line.split(' -> ')
    expr = parts[0].split(' ')
    target = parts[1]
    if 'NOT' in expr:
        circuit[target] = ('not', expr[1])
    elif 'AND' in expr:
        circuit[target] = ('and', expr[0], expr[2])
    elif 'OR' in expr:
        circuit[target] = ('or', expr[0], expr[2])
    elif 'LSHIFT' in expr:
        circuit[target] = ('lshift', expr[0], int(expr[2]))
    elif 'RSHIFT' in expr:
        circuit[target] = ('rshift', expr[0], int(expr[2]))
    elif len(expr) == 1:
        circuit[target] = ('copy', expr[0])
    else:
        assert False, 'invalid instruction: ' + line
print eval_signal_for('a')
