import os
import random
import sys


def read_list(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    if len(lines) == 0:
        return []
    while lines[-1].strip() == '':
        lines = lines[:-1]
    processedLines = [line.strip().lower() for line in lines]
    processedLines.sort()
    return processedLines


def pascalcase(string):
    return ''.join([word[0].upper() + word[1:] for word in string.split()])


def titlecase(string):
    return ' '.join([word[0].upper() + word[1:] for word in string.split()])


def generate_alliterative(prefixList, suffixMapping):
    prefix = random.choice(prefixList)
    suffix = random.choice(suffixMapping[prefix[0]])
    return f'{titlecase(prefix)} {titlecase(suffix)}'


def map_by_first_char(list_to_map):
    output = {}
    for item in list_to_map:
        if item[0] not in output:
            output[item[0]] = []
        output[item[0]].append(item)
    return output


def generate_n_project_names(n):
    adjectives = read_list(f'.{os.sep}data{os.sep}adjectives.txt')
    animals = read_list(f'.{os.sep}data{os.sep}animals.txt')
    animalMapping = map_by_first_char(animals)
    for x in range(n):
        print(generate_alliterative(adjectives, animalMapping))


if __name__ == '__main__':
    n = int(sys.argv[1])
    assert type(n) == int
    generate_n_project_names(n)
