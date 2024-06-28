## Explaining the `test` method:

**1. What are the arguments and what types do these arguments need to have for this function to work?**

    '''
    Arguments are synonymous with parameters. Args are information passed into a function. Different functions will have different numbers of arguments it needs in order to be true and work. E.g. in Excel formulas, if you have an incomplete formula then it won't run because it's missing information needed to calculate. Same goes here.
    The arguments for the function named "test" are "function" and "examples." ... So we should tell it which function we want to evaluate and which examples to evaluate?
    '''


**2. Walk us through the code line by line. What is happening here?**

# KT: What is a kernel? Found here https://stackoverflow.com/questions/47554722/whats-the-relation-between-ipython-jupyter-and-kernels Each notebook works using an instance of a kernel, which is an execution environment that allows to run code in a specific language as well as providing access to some libraries inside the notebook.

# Don't worry about understanding these two lines.
# They are commands we use to get this notebook to autoreload
# so you don't have to rerun your kernel every time you change your homework files.
%load_ext autoreload
%autoreload 2

def test(function, examples):
    passed = 0
    run = 0

    for example in examples:
        run += 1
        expected = example[-1]
        actual = function(*example[:-1])

        if expected == actual: 
            passed += 1
        else:
            print(f"Whoops. For example {example}, the function returned {actual}.")

    print(f"\n{passed} out of {run} examples worked as expected.") 

**3. Does this function have a return value? How do you know?** 
This function will return a printed line that reads This many out of this many run worked as expected, basically.