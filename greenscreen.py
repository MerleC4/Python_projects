from os import _exit as exit

###
### Merle Crutchfield
### This code is used to create a new PPM file that contains the values of the
### mixed two files given as inputs. This is done by asking the user for
### several inputs, the color channel, color channel difference, two image
### files, and the output file. It makes sure that the color channel is r, g,
### or b, and the difference is between 1.0 and 10.0. It also ensures that
### the two files have the same width and height dimensions. Afterwards, it
### iterates through each of the color values, and compares the one specified
### with the other two colors in the pixel * channel difference. If the
### specified pixel color is greater than both, it uses the fill pixel, but if
### not then it uses the greenscreen image pixel. Afterwards, it has all these
### values stored in a 3d list, and then writes them to the new file that the
### user enters the name of.
###

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixels is representd by a list of three ints, which are the RGB values
    of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])
    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)
    return pixels

def new_image(channel, channel_difference, pixels_gs, pixels_fi, pixels):
    '''
    This function is used to create the 3d list of color values for the new
    image being made. The inputs are the channel value, the difference, the
    3d list of greenscreen color values, the 3d list of fill image color values,
    and the pixels list that is empty. The code has an if statement that checks
    the channel letter, and from there iterates through all the values of the
    greenscreen list. It checks to see if the value of the channel pixel color
    is greater than both the other two color values times the channel difference.
    If it is, then it uses the fill image color value for the new list, and if not
    then it uses the greenscreen color value.
    '''
    if channel == 'r':
        for i in range(0, len(pixels_fi)):
            line = []
            for j in range(0, len(pixels_fi[0])):
                if (pixels_gs[i][j][0] > pixels_gs[i][j][1]*channel_difference
                   and pixels_gs[i][j][0] > pixels_gs[i][j][2]*channel_difference):
                    line.append(pixels_fi[i][j])
                else:
                    line.append(pixels_gs[i][j])
            pixels.append(line)
    elif channel == 'g':
        for i in range(0, len(pixels_fi)):
            line = []
            for j in range(0, len(pixels_fi[0])):
                if (pixels_gs[i][j][1] > pixels_gs[i][j][0]*channel_difference
                   and pixels_gs[i][j][1] > pixels_gs[i][j][2]*channel_difference):
                    line.append(pixels_fi[i][j])
                else:
                    line.append(pixels_gs[i][j])
            pixels.append(line)
    else:
        for i in range(0, len(pixels_fi)):
            line = []
            for j in range(0, len(pixels_fi[0])):
                if (pixels_gs[i][j][2] > pixels_gs[i][j][0]*channel_difference
                   and pixels_gs[i][j][2] > pixels_gs[i][j][1]*channel_difference):
                    line.append(pixels_fi[i][j])
                else:
                    line.append(pixels_gs[i][j])
            pixels.append(line)

def create_image(pixels, out_file, size_fi):
    '''
    This function is used to write the PPM file that the user enters the info
    for. It takes in three arguments, the first being the 3d list of numbers
    for the colors, the second being the file name, and the third being the
    size of the new file, since it will be the same as the two entered. It then
    opens a file with the name, write P3 on the first line for the image format
    then the width and height, and then the max color brightness, always 255.
    Then, it goes through the 3d list and will write each line correctly in the
    file, before closing it once completed.
    '''
    fopen = open(out_file, 'w')
    fopen.write('P3\n')
    fopen.write(size_fi + '\n')
    fopen.write('255\n')
    for i in range(0, len(pixels)):
        for j in range(0, len(pixels[0])):
            fopen.write(str(pixels[i][j][0]) + ' ')
            fopen.write(str(pixels[i][j][1]) + ' ')
            fopen.write(str(pixels[i][j][2]) + ' ')
        fopen.write('\n')
    fopen.close()

def main():
    pixels = []
    # Getting user inputs and checking to make sure valid
    channel = input('Enter color channel\n')
    if ((channel != 'r') and (channel != 'g') and (channel != 'b')):
        print('Channel must be r, g, or b. Will exit.')
        exit(0)
    channel_difference = float(input('Enter color channel difference\n'))
    if ((channel_difference > 10.0) or (channel_difference < 1.0)):
        print('Invalid channel difference. Will exit.')
        exit(0)
    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')
    size_gs = get_image_dimensions_string(gs_file)
    size_fi = get_image_dimensions_string(fi_file)
    if (size_gs != size_fi):
        print('Images not the same size. Will exit.')
        exit(0)
    out_file = input('Enter output file name\n')
    # Loads the two image files
    pixels_gs = load_image_pixels(gs_file)
    pixels_fi = load_image_pixels(fi_file)
    # Get new 3D list of pixels
    new_image(channel, channel_difference, pixels_gs, pixels_fi, pixels)
    # Creates the image file, and ends
    create_image(pixels, out_file, size_fi)
    print('Output file written. Exiting.')

# Starts the code
main()
