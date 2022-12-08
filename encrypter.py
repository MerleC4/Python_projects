import random

### Merle Crutchfield
### This code is used to encrypt the lines within a textfile. It will also
### create a textfile that has the scrambled lines, along with another one
### that has the index values of where each line should go. It uses the
### random seed of 125 to make sure that it is consistent, and asks for the
### user to enter a file to encrypt. From there, it reads the contents of
### the file, puts them into a list, switches two line values 5 * line count
### times, and then prints out the new content along with the indexes into
### two new text files.
###

def swap_values(lines, index):
    '''
    This function is used to switch two values of the lists that contain the
    line numbers and the line content themselves. It is ran using a while loop
    that iterates 5 * line count of the file times. It will pick two random
    numbers between 0 and line number - 1, which are indexes of the lists, and
    it will switch the two values in both lists. It uses the lines and index
    lists as arguments, and saves the switched list back to the main function.
    '''
    i = 0
    while i < 5 * len(lines):
        random_one = random.randint(0, len(lines) - 1)
        random_two = random.randint(0, len(lines) - 1)
        lines[random_one], lines[random_two] = lines[random_two], \
            lines[random_one]
        index[random_one], index[random_two] = index[random_two], \
            index[random_one]
        i += 1

def main():
    random.seed(125)
    j = 0; index = []

    # Get the user input for file name, create other fiels
    file = input("Enter a name of a text file to encrypt:\n")
    fopen = open(file, "r")
    output = open("encrypted.txt", "w")
    index_output = open("index.txt", "w")

    # Get rid of newline character, or else it will print twice
    lines = fopen.readlines()
    for line in lines:
        line.strip("\n")
    # Creating list of indexes
    while j < len(lines):
        index.append(j + 1)
        j += 1

    # Calls function that switches two values 5 * line count
    swap_values(lines, index)

    # Writes out values in text files
    for line in lines:
        output.write(line)
    for i in index:
        index_output.write(str(i) + "\n")

    # Closes files
    fopen.close()
    output.close()
    index_output.close()

main()
