
### Merle Crutchfield
### This program is used to take in data from a csv file and to find the
### minimum, maximum, or average in a column that the user enters. This is done
### by asking the user for three inputs: the file name, the column, and the
### operation. Once entered, the code opens the file, splits it by on commas,
### adds each of the values to a 2D list, and then sees which operation was
### entered. Based on that, it goes to a different function where the value is
### calculated, and the final result is printed out.
###


def min(numbers, column):
    '''
    This function is used to find the minimum value in a particular column. The
    arguments are the 2D list, where each row is a line in the csv file, and
    the column is determined by the second argument entered by the user. The
    code sets a variable to the corresponding value of row 0 and column entered
    by user, and then checks all the rest to see if they are less. If they are,
    then the value switches, and the final answer is printed out below.
    '''
    minimum = float(numbers[0][column])
    for i in range(0, len(numbers)):
        num = float(numbers[i][column])
        if num < minimum:
            minimum = num
    print('The minimum value in column', column + 1, 'is:', minimum)

def max(numbers, column):
    '''
    This function is very similar to the previous, except it finds the maximum
    value of the column entered by the user. The arguments are similarly the
    2D list and the column number. The max is initialized to the first
    corresponding value of row 0 and column enterd by user. It then checks the
    rest of the numbers in the column, and if they are greater then it switches
    it, and then the final answer is printed out.
    '''
    maximum = float(numbers[0][column])
    for i in range(0, len(numbers)):
        num = float(numbers[i][column])
        if num > maximum:
            maximum = num
    print('The maximum value in column', column + 1, 'is:', maximum)

def avg(numbers, column):
    '''
    This function is used to calculate the average of the column entered by the
    user. The arguments are the 2D list of numbers, and the column entered by
    the user. The code sets an accumulator to 0, and then adds each value in
    the corresponding column to it. It then calculates the average by taking
    the total and subtracting it by the column count. It prints out the average
    value afterwards.
    '''
    total = 0
    for i in range(0, len(numbers)):
        total += float(numbers[i][column])
    average = total / len(numbers)
    print('The average for column', column + 1, 'is:', average)

def main():
    # Initializing 2D array
    numbers = []
    # Getting inputs
    file = input('Enter CSV file name:\n')
    fopen = open(file, 'r')
    column = input('Enter column number:\n')
    operation = input('Enter column operation:\n')
    # Adding each line to array
    for line in fopen:
        line = line.strip('\n')
        line = line.split(',')
        numbers.append(line)
    # Checking which function to go to
    if operation == 'min':
        min(numbers, int(column) - 1)
    elif operation == 'max':
        max(numbers, int(column) - 1)
    else:
        avg(numbers, int(column) - 1)

# Starts the code
main()
