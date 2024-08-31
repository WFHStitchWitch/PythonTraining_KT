import random #import Python's Random module from the built-in standard library, because I can't be bothered to make up my own sequences of numbers for this function.

list(string_1): []
list(string_2): [] 
#establish a sequence variable named string_1 with type list, starting with nothing in it
random.randint(-1000, 1001) #want to run a random number generator a bunch of times and then add the generated integers into string_1 and also string_2.

#s.append(x) operation

#need the operations to repeatedly add generated integers to the list variables so they are filled with a different count of figures to play with during the processing of the find_twos function.

#Caution: randint function generates floating point numbers; need to convert them to integers before adding to the lists. 

#x in s operation on a string to return true/false if 2 is in sequence for each item in the sequence? 

def find_twos(string_1, string_2):
    '''
        This function takes in two strings that only contains integers, commas and whitespace and
        returns a list of integers, where each integer,

           1. Appears in both strings
           2. Contains a 2 as a digit in the number.

        Inputs:
            str1, str2 (string): strings that contains integers, commas, and whitespace. You can assume each integer is separated by a single comma followed by zero or more whitespaces.

        Output:
            A list of integers, where the list contents is described by above. The returned list must not contain duplicates.
        '''
    pass