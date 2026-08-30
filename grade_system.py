mark = int(input("Enter a mark (0-100): "))

if 0 <= mark <= 100:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "E"

    print(f"Mark: {mark} | Grade: {grade}")
else:
    print("Please enter a mark between 0 and 100.")