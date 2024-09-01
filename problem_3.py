'''import random #import Python's Random module from the built-in standard library, because I can't be bothered to make up my own sequences of numbers for this function.'''

list(string_1) [1, 2, 20, 22, 44, 99]
list(string_2) [3, 5, 22, 100, 44, 2] 
#establish some variables named string_1 and string_2, which are lists, with items in the lists taken out of the example homework problem details.

'''random.randint(-1000, 1001) #want to run a random number generator a bunch of times and then add the generated integers into string_1 and also string_2.

#s.append(x) operation
'''
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
---------------------------------------------------------------------
enumerate(string_1, start=0)
		two_a = 2
		for elem in string_1:
			yield two_a, elem 

'''trying to use enumerate to loop through string_1 and yield elements that equal 2?'''

enumerate(string_2, start=0)
	two_b=2
	for elem in string_2:
		yield two_b, elem

for 2 in string_1 and string_2:
	return