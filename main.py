import sys
import math
import numpy as np



def readFile(filename):
    '''
    Method for reading files and then outputs the parameters for the algorithm and an array of numbers.
    The value of the array is 0 for T and 1 for M
    '''

    with open(filename, 'r') as file:
        print(file.name)
        parameters = file.readline()
        rows , cols , min_ingredients , max_cells = [int(n) for n in parameters.split()]

        pizza = np.zeros([ rows , cols ])
        for row in range(rows):
            for ingredient , col in zip(file.readline(), range(cols)):
                if ingredient == 'T':
                    pizza[row,col] = 0
                if ingredient == 'M':
                    pizza[row,col] = 1

        return pizza, min_ingredients, max_cells



def writeFile(filename, string):
    '''
    Method for writing the solution file
    '''

    with open(filename, 'w') as file:
        file.write(string)




#########################################################


# First the input has to be converted into an array
pizza, min_ing, max_cells = readFile('data/small.in')

print(pizza)
print(min_ing)
print(max_cells)

# Second the pizza has to be sliced up in pieces that fullfil the requirements

# Third the slices have to be written to an outputfile
filename = 'output/test.txt'
string = 'This is an absolutely crazy text!'

writeFile(filename, string)

file = open(filename, 'r')
output = file.readline()
print(output)
