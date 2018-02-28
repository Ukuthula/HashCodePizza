import sys
import numpy as np

print('hello')

with open(sys.argv[1], 'r') as file:
    print(file.name)
    parameters = file.readline()
    rows, cols, min_ing, max_cells = [ int(n) for n in parameters.split()]
    print(rows)
    print(cols)
    print(min_ing)
    print(max_cells)

    pizza = np.zeros([ rows , cols ])
    for row in range(rows):
        for ingredient , col in zip(file.readline(), range(cols)):
            if ingredient == 'T':
                pizza[row,col] = 0
            if ingredient == 'M':
                pizza[row,col] = 1

    print(pizza)
