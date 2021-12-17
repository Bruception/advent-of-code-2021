import sys
from math import prod

operator_map = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda c: int(c[0] > c[1]),
    6: lambda c: int(c[0] < c[1]),
    7: lambda c: int(c[0] == c[1]),
}

class ExpressionNode:
    def __init__(self, type_id):
        self.type_id = type_id
        self.value = 0
        self.children = []

    def evaluate(self):
        if (self.type_id == 4):
            return self.value

        operator_function = operator_map[self.type_id]
        return operator_function([child.evaluate() for child in self.children])

def parse(binary_string, root, bit_index=0):
    # Packet Header
    packet_version = binary_string[bit_index:bit_index+3]
    type_id = int(binary_string[bit_index+3:bit_index+6], 2)
    bit_index += 6

    new_root = ExpressionNode(type_id)

    if (type_id == 4): # Literal Value
        value = ''

        while (binary_string[bit_index] == '1'):
            value += binary_string[bit_index+1:bit_index+5]
            bit_index += 5

        value += binary_string[bit_index+1:bit_index+5]
        bit_index += 5
        
        new_root.value = int(value, 2)
    else: # Operator
        length_type_id = binary_string[bit_index]
        bit_index += 1

        field_length = 15 if length_type_id == '0' else 11

        remaining = int(binary_string[bit_index:bit_index+field_length], 2)
        bit_index += field_length

        while (remaining > 0):
            subpacket_length = parse(binary_string, new_root, bit_index) - bit_index
            bit_index += subpacket_length
            remaining -= subpacket_length if field_length == 15 else 1
    
    root.children.append(new_root)

    return bit_index

hex_string = open(f'{sys.path[0]}/input.txt', 'r').readline()
binary_string = format(int(hex_string, 16), f'0>{len(hex_string) * 4}b')

root = ExpressionNode(0)
parse(binary_string, root)

print(root.evaluate())
