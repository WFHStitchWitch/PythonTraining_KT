import random
def generate_string_1(count1, start, end):
    random.seed(42) #set a fixed seed so the randomizer won't run again every time the code runs. 42 is arbitrary, giving it a seed value.
    string_1 = []
    for _ in range(count1):
        string_1.append(random.randint(start,end))
    return string_1
def generate_string_2(count2, start, end):
    random.seed(13) #set a fixed seed so the randomizer won't run again every time the code runs. 13 is arbitrary, giving it a seed value.
    string_2 = []
    for _ in range(count2):
        string_2.append(random.randint(start,end))
    return string_2
count1 = 20
count2 = 15
start = -1000
end = 1001
string_1 = generate_string_1(count1, start, end)
string_2 = generate_string_2(count2, start, end)
print(f"The first string of integers includes {string_1}.")
print(f"The second string of integers includes {string_2}.")
#Works! Have randomized strings of integers, of different lengths.

#x in s operation on a string to return true/false if 2 is in sequence for each item in the sequence?
#trying to use enumerate to loop through string_1 and yield elements that equal 2?
'''def twos_seeker_v1():
    string_1_collectthetwos = []
    string_2_collectthetwos = []
    for index, char in enumerate(string_1):
        if '2' in char:
            string_1_collectthetwos.append()
    for index, char in enumerate(string_2):
        if '2' in char:
            string_2_collectthetwos.append()
            
            This one did not work

string_1_collectthetwos = twos_seeker
string_2_collectthetwos = twos_seeker

print(string_1_collectthetwos)
print(string_2_collectthetwos)
'''

#Had the enumerate function and filter function up in the documentation and wasn't sure which one to use.
def twos_seeker_v2():
    string_1_filtered = []
    for index, item in enumerate(string_1):
        if '2' in str(item):
            string_1_filtered.append(item)
    return string_1_filtered
    
string_1_filtered = twos_seeker_v2()
print(f"After filtering string one, we get {string_1_filtered}.")

def twos_seeker_v2b():
    string_2_filtered = []
    for index, item in enumerate(string_2):
        if '2' in str(item):
            string_2_filtered.append(item)
    return string_2_filtered
    
string_2_filtered = twos_seeker_v2b()
print(f"After filtering string two, we get {string_2_filtered}.")
#Not very concise to create two functions that do the same thing, but operate on different strings. However, this works in filtering string 1 into its items that contain the character 2 and the same for string 2.
'''
def find_twos():
    found_twos = []
    for item in string_1_filtered:
        if not in string_2_filtered
            found_twos.append(item)
    for item in string_2_filtered:
        if item is not in string_1_filtered
            found_twos.append(item)        
    return found_twos
   This one didn't work. '''


def find_twos_v2(string_1, string_2):
    found_twos_v2 = []
    for index, item in enumerate(string_1):
        if '2' in str(item):
            found_twos_v2.append(item)
    for index, item in enumerate(string_2):
        if '2' in str(item):
            found_twos_v2.append(item)
    return found_twos_v2

found_twos_v2 = find_twos_v2(string_1, string_2)
print(found_twos_v2)
#This one works for those specific strings passing through as arguments.

find_twos_examples = [
    ("", "", []),
    ("1", "1, 3", []),
    ("2", "", []),
    ("2", "1, 3", []),
    ("2", "2", [2]),
    ("2", "12", []),
    ("12", "2, 12", [12]),
    ("1, 3, 5, 12, 7, 200", "2, 6, 9, 200, 5", [200]),
    ("1, 2, 20, 22, 44, 99", "3, 5, 22, 100, 44, 2", [2, 22]),
    ("1,2, 20,22, 44, 99", "3,5, 22, 100, 44, 2", [2, 22]),
    ("1,2, 20,22, 22,44, 20, 99", "3,5, 22, 100, 44, 2", [2, 22]),
    ("1, 2, 20, 22", "3, 2, 20, 22", [2, 20, 22]),
]
#Struggling to create a version that will work on the find_twos_examples item, that seems to hold a bunch of lists inside itself. Briefly tried to make it work without arguments listed in the definition of the find_twos function, but accessing global variables instead of named variables in the function arguments is confusing to implement without errors that it can't find something. Copilot explained it that accessing global variables is also considered imprecise and makes for less legible, modular code.

def find_twos_v3(string_3, string_4):
    found_twos_v3 = []
    for index, item in enumerate(string_3):
        if '2' in str(item):
            found_twos_v3.append(item)
    for index, item in enumerate(string_4):
        if '2' in str(item):
            found_twos_v3.append(item)
    return found_twos_v3

string_3 = [1, 2, 20, 22, 33, 99]
string_4 = [3, 5, 22, 100, 44, 2]

found_twos_v3 = find_twos_v3(string_3, string_4)
print(found_twos_v3)
#Not entirely correct; it pulls out the 2s and writes them into one list, but fails to filter duplicates. My randomized strings 1 and 2 did not have any duplicates, so this function needs something added on to remove duplicates before the final return of the found twos list variable.

def find_twos_v4(string_3, string_4):
    '''
    This function takes in two strings that only contain integers, commas, and whitespace and
    returns a list of integers, where each integer,

       1. Appears in both strings
       2. Contains a 2 as a digit in the number.

    Inputs:
        string_1, string_2 (string): strings that contain integers, commas, and whitespace. You can assume each integer is separated by a single comma followed by zero or more whitespaces.

    Output:
        A list of integers, where the list contents are described above. The returned list must not contain duplicates.
    '''
    found_twos_v4 = []
    for index, item in enumerate(string_3):
        if '2' in str(item):
            found_twos_v4.append(item)
    for index, item in enumerate(string_4):
        if '2' in str(item):
            if item not in string_3:
                found_twos_v4.append(item)
    return found_twos_v4

string_3 = [1, 2, 20, 22, 33, 99]
string_4 = [3, 5, 22, 100, 44, 2]

found_twos_v4 = find_twos_v4(string_3, string_4)
print(found_twos_v4)


def find_twos_final(string_3, find_twos_examples):
    '''
    This function takes in two strings that only contain integers, commas, and whitespace and
    returns a list of integers, where each integer,

       1. Appears in both strings
       2. Contains a 2 as a digit in the number.

    Inputs:
        string_1, string_2 (string): strings that contain integers, commas, and whitespace. You can assume each integer is separated by a single comma followed by zero or more whitespaces.

    Output:
        A list of integers, where the list contents are described above. The returned list must not contain duplicates.
    '''
    found_twos_v5 = []
    for index, item in enumerate(string_3):
        if '2' in str(item):
            found_twos_v5.append(item)
    for index, item in enumerate(find_twos_examples):
        if '2' in str(item):
            if item not in string_3:
                if item not in found_twos_v5:
                    found_twos_v5.append(item)
    return found_twos_v5

string_3 = [1, 2, 20, 22, 33, 99]
string_4 = [3, 5, 22, 100, 44, 2]

found_twos_v5 = find_twos_final(string_3, find_twos_examples)
print(found_twos_v5)

def test(function, examples):
    passed = 0
    run = 0

    for example in examples:
        run += 1
        expected = example[-1]
        actual = find_twos_v4(*example[:-1])

        if expected == actual: 
            passed += 1
        else:
            print(f"Whoops. For example {example}, the function returned {actual}.")

    print(f"\n{passed} out of {run} examples worked as expected.")

find_twos_v5 = test(function=find_twos_v4, examples=find_twos_examples)
print(find_twos_v5)

''' Very uncertain I'm using the find_twos_examples input correctly. Can get the answer correct with the two sample strings at the beginning of the problem, but testing with the large data set in find_twos_examples throws the Whoops return.'''