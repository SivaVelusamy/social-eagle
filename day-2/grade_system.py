"""Convert a numeric mark into a letter grade.

This script prompts the user for a mark between 0 and 100, validates the
input, and prints the corresponding grade.
"""

# Prompt the user to enter a mark from 0 to 100, then remove surrounding whitespace.
user_input = input("Enter a mark between 0 and 100: ").strip()

# Attempt to convert the user's input into a float so numeric comparisons
# can be performed safely.
try:
    mark = float(user_input)
except ValueError:
    # Inform the user that the value cannot be interpreted as a number.
    print(f"Invalid input: '{user_input}' is not a number.")
    mark = None

if mark is None:
    pass
elif not 0 <= mark <= 100:
    print(f"Invalid input: {mark} is outside the range 0 to 100.")
else:
    if 90 <= mark <= 100:
        grade = "A"
    elif 80 <= mark <= 89:
        grade = "B"
    elif 70 <= mark <= 79:
        grade = "C"
    elif 60 <= mark <= 69:
        grade = "D"
    else:
        grade = "E"

    # Display the final mark rounded to a whole number and its letter grade.
    print(f"Mark: {mark:.0f} -> Grade: {grade}")
