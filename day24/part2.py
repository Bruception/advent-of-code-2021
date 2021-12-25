import sys
from functools import cache

program = [line.strip().split() for line in open(f'{sys.path[0]}/input.txt', 'r')]
n = len(program)
max_value = 10 ** 7

@cache
def solve(i, w, x, y, z):
    if (z >= max_value):
        return (False, 0)
    if (i >= n):
        return (z == 0, '')

    instruction = program[i]
    variables = {'w': w, 'x': x, 'y': y, 'z': z}
    op_code, arg1 = instruction[0], instruction[1]
    
    if (op_code == 'inp'):
        for digit in range(1, 11):
            variables[arg1] = digit
            good, number = solve(i + 1, **variables)
            if (good):
                return (True, f'{digit}{number}')
        
        return (False, 0)
    
    arg2 = instruction[2]
    arg2 = variables[arg2] if arg2.isalpha() else int(arg2)

    if (op_code == 'add'):
        variables[arg1] += arg2
    if (op_code == 'mul'):
        variables[arg1] *= arg2
    if (op_code == 'div'):
        if (arg2 == 0):
            return (False, 0)
        variables[arg1] //= arg2
    if (op_code == 'mod'):
        if (variables[arg1] < 0 or arg2 <= 0):
            return (False, 0)
        variables[arg1] %= arg2
    if (op_code == 'eql'):
        variables[arg1] = int(variables[arg1] == arg2)
    
    return solve(i + 1, **variables)

print(int(solve(0, 0, 0, 0, 0)[1]))
