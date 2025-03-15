"""
To run this file issue this command:
python3 HelloWorld.py

Python as a interpreted language executes code directly without a separate compilation step, 
translating and running the source code on-the-fly during execution.
"""

from algorithms import  *

# Checks if the Python script is being run as the main program (not imported as a module)
if __name__ == "__main__":
    lst = [12, 11, 13, 5, 6, 7]
    print("Given array is", lst)

    print("Sorted array is", quick_sort(lst))