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
print(string_1)
print(string_2)
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

#Had the enumerate function and filter function up in the documentation and wasn't sure which one to use. Try with filter function next.
def twos_seeker_v2():
    string_1_filtered = []
    for index, item in enumerate(string_1):
        if '2' in str(item):
            string_1_filtered.append(item)
    return string_1_filtered
    
string_1_filtered = twos_seeker_v2()
print(string_1_filtered)

def twos_seeker_v2b():
    string_2_filtered = []
    for index, item in enumerate(string_2):
        if '2' in str(item):
            string_2_filtered.append(item)
    return string_2_filtered
    
string_2_filtered = twos_seeker_v2b()
print(string_2_filtered)
#Not very concise to create two functions that do the same thing, but operate on different strings. However, this works in filtering string 1 into its items that contain the character 2 and the same for string 2.

