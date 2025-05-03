import re
from itertools import permutations
def calc(exp, op) :
    exp = exp[:]
    for o in op :
        stack = []
        i = 0
        while i < len(exp) :
            if exp[i] == o :
                left = stack.pop()
                right = exp[i + 1]
                if o == '+' :
                    stack.append(left + right)
                elif o == '-' :
                    stack.append(left - right)
                elif o == '*' :
                    stack.append(left * right)
                i += 2
            else :
                stack.append(exp[i])
                i += 1
        exp = stack
    return abs(exp[0])

def solution(expression):
    tokens = re.split(r'(\D)', expression)
    exp = []
    for token in tokens :
        if token in '+-*' :
            exp.append(token)
        else :
            exp.append(int(token))
    op = set([x for x in exp if type(x) is str])
    max_value = 0
    for o in permutations(op) :
        max_value = max(max_value, calc(exp, o))
    return max_value