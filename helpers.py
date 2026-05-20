# helpers.py
# This is a custom module. We import it in main.py using: import helpers
# Modules help usorganise code into separate files so main.py stays clean.abs

import random

#
# TOOL 1 HELPERS: Grade Calculator
#

def get_letter_grade(average):
    """
    Takes a numeric average and returns a letter grade.
    Demonstrates the use of if/elif/else statements.
    """
    if average >= 80:
        return "A - Distinction"
    elif average >= 70:
        return "B - Merit"
    elif average >= 60:
        return "C - Pass"
    elif average >= 50:
        return "D - Below average"
    else:
        return "F - Fail"

def calculate_average(marks):
    """
    Takes a list of marks and returns the average.
    Demonstrates the use of sum() and len() functions.
    """
    if len(marks) == 0:  # Avoid dividing by zero
        return 0
    return sum(marks) / len(marks)

#
# TOOL 2 HELPERS: Even or Odd Checker + Divisibilty
#

def check_even_odd(number):
    """
    Returns True if nummber is divisible by divisor
    Demonstrates: modulus operator, logical operators (and/or)
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def is_divisible_by(number, divisor):
    """
    Returns True if number is divisible by divisor.
    Demonstrates: modulus operator, logical operators (and/or)
    """
    return number % divisor == 0

#
# TOOL 3 HELPERS: Number Guessing Game
#

def generate_secret_number(low=1, high=100):
    """
    Generates a random integer between low and high (inclusive).
    Demonstrates: built-in module (random), parameters with defaulft values.
    """

    return random.randint(low, high)

def give_hint(guess, secret):
    """
    Compares the user's guess to the secret number and returns feedback.
    Demonstrates: if/elif/else statements.
    """
    if guess < secret:
        return "Too low! Try higher"
    elif guess > secret:
        return "Too high! Try lower."
    else:
        return "Correct!"

#
# TOOL 4 HELPERS: TO-DO List
#

def display_tasks(task_list):
    """
    Prints all tasks with a numbered index.
    Demonstrates: for loop, range(), f-strings, enumerate.
    """
    if len(task_list) == 0:
        print("Your to-do list is empty.")
        return
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")

def add_task(task_list, new_task):
    """
Adds a task to the list usinng list.append() method.
Demonstrates: lists, passing a list as an argument (mutable).
    """
    task_list.append(new_task)
    print(f"Added: {new_task}")

def remove_task(task_list, task_number):
    """
Removes a task by its number (1-based index).
Demonstrates: lists, indexing, type casting (int), list.pop().
    """
    index = task_number - 1  # Convert to 1-based to 0-based index
    if 0 <= index < len(task_list):
        removed = task_list.pop(index)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number. Please try again.")

#
# TOOL 5 HELPERS: Daily MOtivation Generator
#

QOUTES = [
    "Believe you can and you're halfway there.",
    "The only way to do great work is to love what you do.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It does not matter how slowly you go as long as you do not stop."
]

def get_random_quote():
    """
Returns a random quote from the QOUTES list.
Demonstrates: lists, random.choice().
    """
    return random.choice(QOUTES)