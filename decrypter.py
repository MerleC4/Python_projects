### Merle Crutchfield
### This code is used to decrypt the file that was encrypted from the encrypter
### code. It asks the user for the index file and the encrypted file, and
### creates a new file for where the decrypted code goes. It reads the content
### of the first two files into lists, and runs through each element using a
### nested while loop. This is because it has to run through each element of
### the length of the index file, for each line, and then for each line it has
### to run through again to find where the corresponding line is. Once it finds
### the next line in order, it writes it into the output file, and then goes to
### the next number. After it finishes, it closes all of the files.
###


def main():
    # Getting encrypted and index files
    file = input("Enter the name of an encrypted text file:\n")
    index_file = input("Enter the name of the encryption index file:\n")

    # Creating decrypted file and opening files entered
    output = open("decrypted.txt", "w")
    fopen = open(file, "r")
    fopen_index = open(index_file, "r")

    # Creating list of content from encrypted and index
    lines = fopen.readlines()
    lines_index = fopen_index.readlines()

    # Nested while loop to run through each element until completed
    i, j = 1, 1
    while i <= len(lines):
        while j <= len(lines):
            if int(lines_index[j - 1][:-1]) == i:
                output.write(lines[j - 1])
                break
            j += 1
        i += 1
        j = 0

    # Closes the files
    output.close()
    fopen.close()
    fopen_index.close()

main()
