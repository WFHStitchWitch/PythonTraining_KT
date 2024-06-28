## Explaining the `test` method:

**1. What are the arguments and what types do these arguments need to have for this function to work?**

Arguments are synonymous with parameters. Args are information passed into a function. Different functions will have different numbers of arguments it needs in order to be true and work. E.g. in Excel formulas, if you have an incomplete formula then it won't run because it's missing information needed to calculate. Same goes here. The arguments for the function named "test" are "function" and "examples." ... So we should tell it which function we want to evaluate and which examples to evaluate?
   


**2. Walk us through the code line by line. What is happening here?**

What is a kernel? Found here https://stackoverflow.com/questions/47554722/whats-the-relation-between-ipython-jupyter-and-kernels Each notebook works using an instance of a kernel, which is an execution environment that allows to run code in a specific language as well as providing access to some libraries inside the notebook.

Don't worry about understanding these two lines.
They are commands we use to get this notebook to autoreload
so you don't have to rerun your kernel every time you change your homework files.

%load_ext autoreload

%autoreload 2

    def test(function, examples): # DEFines a new function named "test" and gives it two arguments. Those arguments are named "function" and "examples."
        passed = 0 # creates a new variable named "passed" and sets its value equal to zero.
        run = 0 # creates a new variable named "run" and sets its value equal to zero.

        for example in examples: # FOR is a flow control trigger that can loop through statements multiple times until done. For the argument named "examples," there are variables named and then an if/else loop to evaluate with those variables. 
            run += 1 # creates a new variable called "run" and assigns it the value of "run+1"
            expected = example[-1] # creates a new variable called "expected" and assigns it the value of a list named example, with one number in the list denoted in square brackets.
            actual = function(*example[:-1])

            if expected == actual: 
                passed += 1 # if the expected variable evaluates as equal to the actual variable, then the passed variable gets a new value of "passed+1", operating to add +1 to the existing value of passed. Passed starts at zero, so running will count up number of passed evaluations when running the test function...?
            else:
                print(f"Whoops. For example {example}, the function returned {actual}.") # if the expected variable evaluates as not equal to the actual variable, then run the print function to print this string. Printing this string will insert the variable values of example and actual into the string upon evaluation. 

        print(f"\n{passed} out of {run} examples worked as expected.") # prints the final evaluation of the test function being run as a string with variable values calculated and inserted. 

**3. Does this function have a return value? How do you know?** 

This function will return a printed line that reads This many out of this many run worked as expected, basically.
