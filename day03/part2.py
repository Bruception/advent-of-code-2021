import sys

def getCandidate(candidates, criteria):
    processing = candidates[::]
    bit = 0

    while (len(processing) > 1):
        ones_count = 0
        for binary_string in processing:
            ones_count += 1 if binary_string[bit] == '1' else 0
        valid = []
        for binary_string in processing:
            if (binary_string[bit] == criteria(ones_count, processing)):
                valid.append(binary_string)
        processing = valid
        bit += 1
    
    return processing[0]

def most_common(ones_count, processing):
    return '1' if ones_count >= len(processing) - ones_count else '0'

def least_common(ones_count, processing):
    return '1' if most_common(ones_count, processing) == '0' else '0'

file = open(f'{sys.path[0]}/input.txt', 'r')
binary_strings = [line.strip() for line in file]

oxygen_generator_rating = int(getCandidate(binary_strings, most_common), base=2)
CO2_scrubber_rating = int(getCandidate(binary_strings, least_common), base=2)

print(oxygen_generator_rating * CO2_scrubber_rating)
