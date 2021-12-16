import sys

def parse(binary_string, bit_index=0):
    global packet_version_total
    # packet_header
    packet_version = binary_string[bit_index:bit_index+3]
    type_id = int(binary_string[bit_index+3:bit_index+6], 2)
    bit_index += 6

    packet_version_total += int(packet_version, 2)

    if (type_id == 4): # Literal Value
        value = ''
        while (binary_string[bit_index] == '1'):
            value += binary_string[bit_index+1:bit_index+5]
            bit_index += 5

        value += binary_string[bit_index+1:bit_index+5]
        bit_index += 5
    else: # Operator
        length_type_id = binary_string[bit_index]
        bit_index += 1

        field_length = 15 if length_type_id == '0' else 11

        remaining = int(binary_string[bit_index:bit_index+field_length], 2)
        bit_index += field_length

        while (remaining > 0):
            subpacket_length = parse(binary_string, bit_index) - bit_index
            bit_index += subpacket_length
            remaining -= subpacket_length if field_length == 15 else 1

    return bit_index

hex_string = open(f'{sys.path[0]}/input.txt', 'r').read()
binary_string = format(int(hex_string, 16), f'0>{len(hex_string) * 4}b')

packet_version_total = 0
parse(binary_string)

print(packet_version_total)
