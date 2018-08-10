
def readFile(file):
    for line in file:
        print(line)

with open('./patterns.txt') as patterns:
    readFile(patterns)