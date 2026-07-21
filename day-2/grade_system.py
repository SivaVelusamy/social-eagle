user_input = input("Enter a mark between 0 and 100: ").strip()

try:
    mark = float(user_input)
except ValueError:
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

    print(f"Mark: {mark:.0f} -> Grade: {grade}")
