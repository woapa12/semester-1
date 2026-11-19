
# PGM functions that we write

def readPGM( filename ):
    ''' 
    Read a named PGM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''

    with open(filename,"r") as f:    # read in the file
        data = f.readlines()
        
    data = [line.strip().split() for line in data[1:]] # clean the space-separated data, skip the first line
          
    width = int(data[0][0]) # store the data - compare to the text in the file
    height = int(data[0][1])
    max_gray = int(data[1][0])
    pixels = [[int(data[2+i][j]) for j in range(width)] for i in range(height)] # nested list comprehension for pixel array
    
    return width,height,max_gray,pixels   # tuple of PGM data
    
def writePGM( filename, image ):
    '''
    Write a PGM file to disk
    Input: filename string, image tuple data
    Output: None
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    # Arrange pixels into rows using it's height and width, then use .split() for all rows to get indivual elements
    pixel_rows = [pixels[row*width : (row+1)*width] for row in range(height-1)]
    pixel_array = [row.split() for row in pixel_rows]
    # Create the string of pixels
    pixel_string = ""
    for row in pixel_array:
        for i in row:
            pixel_string += str(i) + " "
        pixel_string += "\n"

    with open(filename, "w") as f:
        f.write(f"P2\n{width} {height}\n{max_gray}\n{pixel_string}")
    # open a file for writing
    # write the data in PGM format
    # don't forget the PGM code "P2"
    return True

def invertPGM( image ):
    '''
    Invert an image, ie. pixel value = 255 - pixel value
    Input: image data
    Output: inverted image data
    '''
    width,height,max_gray,pixels = image  # unpack the tuple

    inverted_pixels = [max_gray - value for value in pixels]
    # your code
    # create a new pixel array of inverted data 
    inverted = []  # you can use a similar nested comprehension to the readPGM() function
    
    return width,height,max_gray,inverted_pixels

# code to test the PGM functions

image = readPGM("images/feep.pgm")

print(f"Image with width {image[0]} and height {image[1]}")
print(f"{image[3]}")

# write further code to test your own functions
