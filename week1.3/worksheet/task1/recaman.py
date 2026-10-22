# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
sequence = [0]
for i in range(1,L):
    # ak = ak-1 – k if   ak-1 – k > 0 , and this number is not already in the sequence 
    # ak = ak-1 + k

    a = sequence[-1] - i
    if a<0 or a in sequence:
        b = sequence[-1] + i
        sequence.append(b)
    else:
        sequence.append(a)


# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence