# Week 4, Session 1: 

# Your are given the function filter_positive_numbers with a docstring.
# Can you identify the inconsistency between the docstring and the implementation?

# Your task is to update the docstring to reflect what the function does.


def filter_positive_numbers(numbers):
    """
    Filters out negative numbers from the list, keeping only the positive ones.
    The function returns a list of all the positive numbers in the input.

    Args:
        numbers (list of int): A list of integers.

    Returns:
        list of int: A list containing only numbers above 0; that is, positive numbers.
    """
    return [num for num in numbers if num > 0]

numbers = [3.4, -4, 348, -234, 83, -2]

print (filter_positive_numbers(numbers))
