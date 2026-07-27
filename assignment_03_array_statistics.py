# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#
def main():
    print("Fibonacci Sequence Generator")
    print("-----------------------------")
    print("A) Print the first N terms")
    print("B) Check if a number is a Fibonacci number")

    choice = input("\nChoose a part to run (A / B): ").strip().upper()

    if choice == "A":
        n = int(input("How many terms? "))
        print_fibonacci(n)

    elif choice == "B":
        number = int(input("Enter a number to check: "))
        if is_fibonacci(number):
            print(f"{number} is a Fibonacci number.")
        else:
            print(f"{number} is NOT a Fibonacci number.")

    else:
        print("Invalid choice. Please enter A or B.")


if __name__ == "__main__":
    main()

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

