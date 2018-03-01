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
        countT = 0
        countM = 0

        pizza = [[[] for _ in range(cols)] for _ in range (rows) ]
        for row in range(rows):
            for ingredient , col in zip(file.readline(), range(cols)):
                if ingredient == 'T':
                    pizza[row][col] = (0,0,0)
                    countT += 1
                if ingredient == 'M':
                    pizza[row][col] = (1,0,0)
                    countM += 1

        return pizza, rows, cols, min_ingredients, max_cells, countT, countM



def writeFile(filename, string):
    '''
    Method for writing the solution file
    '''

    with open(filename, 'w') as file:
        file.write(string)



def findClosest(row , col , rows, cols, max_d , pizza):
    '''
    Finds out how close the other ingredients are.
    '''
    for x in range(1, max_d):
        if ( row + x < rows ) and ( pizza[row + x][col][0]  !=  pizza[row][col][0] ):
            pizza[row][col] = (pizza[row][col][0], x ,pizza[row][col][2])
            break
        if ( row - x >= 0 ) and ( pizza[row - x][col][0]  !=  pizza[row][col][0] ):
            pizza[row][col] = (pizza[row][col][0], x ,pizza[row][col][2])
            break
        if ( col + x < cols ) and ( pizza[row][col + x][0]  !=  pizza[row][col][0] ):
            pizza[row][col] = (pizza[row][col][0], x ,pizza[row][col][2])
            break
        if ( col - x >= 0 ) and ( pizza[row][col - x][0]  !=  pizza[row][col][0] ):
            pizza[row][col] = (pizza[row][col][0], x ,pizza[row][col][2])
            break

    return pizza



#########################################################


# First the input has to be converted into an array
pizza, rows, cols, min_ing, max_cells, cT, cM = readFile('data/small.in')

print(pizza)
print(min_ing)
print(max_cells)
print('Tomatocount: ' , cT)
print('Mushroomcount: ' , cM)

# Second the pizza has to be sliced up in pieces that fullfil the requirements

pizza = findClosest(5, 0, rows, cols, max_cells, pizza)
print(pizza[5][0])

# Third the slices have to be written to an outputfile
filename = 'output/test.txt'
string = 'This is an absolutely crazy text!'

writeFile(filename, string)

file = open(filename, 'r')
output = file.readline()
print(output)
file.close()
