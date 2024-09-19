
def mean():
    '''
        This function takes in a space-separated string of integers and floats and
        returns a their mean as a float.

        Inputs:
            string_of_numbers (string): a space-separated string of integers and floats.

        Output:
            a float, the mean of the inputted numbers.
        '''
    string_of_numbers = input("Enter a whitespace-separated string of numbers: ")
    numbers = list(map(float, string_of_numbers.split()))
    return sum(numbers) / len(numbers)

print(mean())