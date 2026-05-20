#main.property
#Python Mini Toolkit - My first coding project
#Author:  Siwaphiwe SIboto
#
#This program is amenu based toolkkit with 5 mini tools
#It uses a custom module (helpers.py) and the built in random

import helpers # Import the custom module from helpers.py

#DISPLAY FUNCTION

def print_banner():
    """Prints a welcome banner when the program  starts."""
    print("="* 50)
    print("PYTHON MINI TOOLKIT")
    print("My First Coding Project")
    print("="* 50)
    print()

def print_main_menu():
    """Displays the main menu options to the user."""
    print("\n--- MAIN MENU ---")
    print("1. Grade Calculator")
    print("2. Even or Odd Checker")
    print("3. Number Guessing Game")
    print("4. To-Do List Manager")
    print("5. Daily Motivation Generator")
    print("6. Exit")
    print("-" * 20)

# TOOL 1: Grade Calculator

def grade_calculator():
    """
    Asks the user to enter subject marks, then calcutes their average and letter grades.

    Concepts Used:
    - while loops (to keep asking for marks)
    - type casting: int(input(...))
    - lists (to store marks)
    - functions from helpers module
    - if/else statements for input validation
    """
    print("\n--- GRADE CALCULATOR ---")
    print("Enter your marks one at a time. Type 'done' when finished, or enter 'n' when asked to continue.\n")

    marks = []  # Empty list to store the marks

    while True:
        entry = input("Enter mark (0-100): ").strip()
        if entry.lower() == 'done':
            break
        if entry.isdigit():
            mark = int(entry)
            if 0 <= mark <= 100:
                marks.append(mark)
                print(f"Mark {mark} added.")
            else:
                print("Please enter a valid mark between 0 and 100.")
                continue
        else:
            print("Invalid input. Please enter a number or 'done'.")
            continue

        again = input("Would you like to add another mark? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            break

    if len(marks) == 0:
        print("No marks entered. Returning to main menu.")
        return

    average = helpers.calculate_average(marks)
    grade = helpers.get_letter_grade(average)

    print(f"\nMarks entered: {marks}")
    print(f"Average: {average:.1f}%")
    print(f"Letter Grade: {grade}")

# TOOL 2: Even or Odd Checker

def even_odd_checker():
    """
    Asks the user to enter a number and checks if it's even or odd.

    Concepts Used:
    - type casting: int(input(...))
    - for loop with range()
    - modulus operator (%) inside helpers
    - logical operators: and / or
    """
    print("\n--- EVEN OR ODD CHECKER ---")
    try:
        count = int(input("How many numbers do you want to check? "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    for i in range(count):
        try:
            num = int(input(f"Enter number {i + 1}: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        result = helpers.check_even_odd(num)
        div3 = helpers.is_divisible_by(num, 3)
        div5 = helpers.is_divisible_by(num, 5)

        print(f"{num} is {result}.", end=' ')
        if div3 and div5:
            print("It is also divisible by both 3 and 5.")
        elif div3 or div5:
            divisor = "3" if div3 else "5"
            print(f"It is also divisible by {divisor}.")
        else:
            print()

# TOOL 3: Number Guessing Game

def number_guessing_game():
    """
    A simple number guessing game where the user tries to guess a random number between 1 and 100.

    Concepts Used:
    - random module (helpers.generate_secret_number())
    - while loop
    - type casting: int(input(...))
    - if/else statements for feedback
    """
    print("\n--- NUMBER GUESSING GAME ---")
    print("I have selected a random number between 1 and 100. Can you guess it?\n")

    secret = helpers.generate_secret_number(1, 100)
    attempts = 0
    max_tries = 10

    while attempts < max_tries:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_tries}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        attempts += 1
        hint = helpers.give_hint(guess, secret)
        print(hint)

        if guess == secret:
            print(f"You got it in {attempts} attempt(s)!")
            return

    print(f"Sorry, you've used all {max_tries} attempts. The number was {secret}. Better luck next time!")

# TOOL 4: To-Do List Manager

def todo_list_manager():
    """
    A simple to-do list manager that allows users to add, view, and remove tasks.

    Concepts Used:
    - while loop with nested if / elif / else
    - lists add, remove, display
    - type casting: int(input(...))
    - functions with list as argument
    """
    print("\n--- TO-DO LIST MANAGER ---")
    tasks = []  # our to do list starts empty

    while True:
        print("\n a) View tasks")
        print(" b) Add a task")
        print(" c) Remove a task")
        print(" d) Back to main menu")

        choice = input("Enter your choice (a-d): ").strip().lower()

        if choice == "a":
            print()
            helpers.display_tasks(tasks)
        elif choice == "b":
            new_task = input("Enter a new task: ").strip()
            if new_task:
                helpers.add_task(tasks, new_task)
            else:
                print("Task cannot be empty.")
        elif choice == "c":
            helpers.display_tasks(tasks)
            if len(tasks) > 0:
                try:
                    num = int(input("Enter the number of the task to remove: "))
                    helpers.remove_task(tasks, num)
                except ValueError:
                    print("Invalid input. Please enter a whole number.")
        elif choice == "d":
            break
        else:
            print("Invalid choice. Please enter a, b, c, or d.")

# TOOL 5: Daily Motivation Generator

def motivation_generator():
    """
    Generates a random motivational quote for the user.

    Concepts Used:
    - while loop
    - random.choice() from helpers
    - lists (QOUTES defined in helpers.py)
    - user input / boolean expression
    """
    print("\n--- DAILY MOTIVATION GENERATOR ---")

    keep_going = True

    while keep_going:
        quote = helpers.get_random_quote()
        print(f"\nMotivational Quote: {quote}\n")

        again = input("Would you like another quote? (y/n): ").strip().lower()
        if again not in ("yes", "y"):
            keep_going = False

    print("Stay motivated! See you next time.")

# MAIN FUNCTION - Entry point of the program

def main():
    """
    Controls the main menu loop.
    Demonstrates: while loop, if/elif/else, calling functions.
    """
    print_banner()

    running = True  # Boolean variable to control the main loop

    while running:
        print_main_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            grade_calculator()
        elif choice == "2":
            even_odd_checker()
        elif choice == "3":
            number_guessing_game()
        elif choice == "4":
            todo_list_manager()
        elif choice == "5":
            motivation_generator()
        elif choice == "6":
            print("\nExiting the toolkit. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# This block only runs when you execute main.py directly.
# It does not run if another file imports main.py as a module.
if __name__ == "__main__":
    main()
