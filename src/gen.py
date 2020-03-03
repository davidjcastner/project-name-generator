'''
gen.py
    takes an integer as input and creates that many
    alliterative animal project names
'''

import os
import random
import sys


def read_list(filename):
    '''reads a text file where each line is an item in a list'''
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
    '''converts a string to PascalCase'''
    return ''.join([word[0].upper() + word[1:] for word in string.split()])


def titlecase(string):
    '''converts a string to Title Case'''
    return ' '.join([word[0].upper() + word[1:] for word in string.split()])


def generate_alliterative(prefixList, suffixMapping):
    '''combines a list of prefixes with a suffix starting with same char'''
    prefix = random.choice(prefixList)
    suffix = random.choice(suffixMapping[prefix[0]])
    return f'{titlecase(prefix)} {titlecase(suffix)}'


def map_by_first_char(list_to_map):
    '''creates a dictionary where the first char is the key'''
    output = {}
    for item in list_to_map:
        if item[0] not in output:
            output[item[0]] = []
        output[item[0]].append(item)
    return output


def generate_n_project_names(n):
    '''full process for generating project names'''
    adjectives = read_list(f'.{os.sep}data{os.sep}adjectives.txt')
    animals = read_list(f'.{os.sep}data{os.sep}animals.txt')
    animalMapping = map_by_first_char(animals)
    for x in range(n):
        print(generate_alliterative(adjectives, animalMapping))


if __name__ == '__main__':
    n = int(sys.argv[1])
    assert type(n) == int
    generate_n_project_names(n)
