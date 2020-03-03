import os
import random
import sys


def readfile(filename):
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


def generateAlliterative(prefixList, suffixMapping):
    prefix = random.choice(prefixList)
    suffix = random.choice(suffixMapping[prefix[0]])
    return f'{titlecase(prefix)} {titlecase(suffix)}'


def mapByStartingCharacter(input):
    output = {}
    for item in input:
        if item[0] not in output:
            output[item[0]] = []
        output[item[0]].append(item)
    return output


def generateNProjectNames(n):
    adjectives = readfile(f'.{os.sep}data{os.sep}adjectives.txt')
    animals = readfile(f'.{os.sep}data{os.sep}animals.txt')
    animalMapping = mapByStartingCharacter(animals)
    for x in range(n):
        print(generateAlliterative(adjectives, animalMapping))


if __name__ == '__main__':
    n = int(sys.argv[1])
    assert type(n) == int
    generateNProjectNames(n)
