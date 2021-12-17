import sys

def parse(bits, i=0):
    global packet_version_total
    # Packet Header
    packet_version = bits[i:i+3]
    type_id = int(bits[i+3:i+6], 2)
    i += 6

    packet_version_total += int(packet_version, 2)

    if (type_id == 4): # Literal Value
        value = ''

        while (bits[i] == '1'):
            value += bits[i+1:i+5]
            i += 5

        value += bits[i+1:i+5]
        i += 5
    else: # Operator
        length_type_id = bits[i]
        i += 1

        field_length = 15 if length_type_id == '0' else 11

        remaining = int(bits[i:i+field_length], 2)
        i += field_length

        while (remaining > 0):
            subpacket_length = parse(bits, i) - i
            i += subpacket_length
            remaining -= subpacket_length if field_length == 15 else 1

    return i

hex_string = open(f'{sys.path[0]}/input.txt', 'r').read()
bits = format(int(hex_string, 16), f'0>{len(hex_string) * 4}b')

packet_version_total = 0
parse(bits)

print(packet_version_total)
