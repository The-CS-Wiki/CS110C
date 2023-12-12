#
#  Author: Benjamin Herrera
#
#  CS110C // Basics of Python
#  Chapter X: Variables
#  Practice X
#

# Imports
import sys
import importlib
import io
from contextlib import redirect_stdout


# Main function
def main():
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python check.py <problem_number>")
        sys.exit(1)

    # Get the problem number and module_name
    prob_num = sys.argv[1]
    module_name = f"problem{prob_num}"

    # Try to import the file
    try:
        # Dynamically import the specified problem module
        problem_module = importlib.import_module(module_name)

    # If an error occurred, show error
    except ImportError:
        print(f"Module {module_name}.py not found.")
        sys.exit(1)

    # Capture the output of the problem module
    f = io.StringIO()
    with redirect_stdout(f):
        problem_module.main()
    output_lines = f.getvalue().strip().split("\n")

    # Read the expected output from a text file and split into lines
    try:
        with open(f"./answers/expected{prob_num}.txt", "r") as file:
            expected_lines = file.read().strip().split("\n")
    except FileNotFoundError:
        print(f"\nExpected output file for problem {prob_num} not found.\n")
        sys.exit(1)

    # Compare and print results
    for i, (actual, expected) in enumerate(zip(output_lines, expected_lines)):
        if actual != expected:
            print(f"\nAnswer {i + 1} is incorrect\n")
            break
    else:
        if len(output_lines) == len(expected_lines):
            print("\nAll lines match the expected result!")
            print(
                """
         _______________
        |@@@@|     |####|
        |@@@@|     |####|
        |@@@@|     |####|
        \\@@@@|     |####/
         \\@@@|     |###/
          `@@|_____|##'
               (O)
            .-'''''-.
          .'  * * *  `.
         :  *       *  :
        : ~  Problem  ~ :
        : ~ Completed ~ :
         :  *       *  :
          `.  * * *  .'
            `-.....-'
              \n"""
            )
        else:
            print("\nOutput length does not match the expected result.\n")


# Main process
if __name__ == "__main__":
    main()
