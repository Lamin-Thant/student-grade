student_name = input("Enter student name: ")

first_mark = float(input("Enter first subject mark: "))
second_mark = float(input("Enter second subject mark: "))

total_mark = first_mark+second_mark
average_mark = (first_mark + second_mark) / 2


if average_mark >= 50:
    result = "Pass"
else:
    result = "Fail"

print("\nStudent Name:", student_name)
print("Total Mark:",total_mark)
print("Average Mark:", average_mark)
print("Result:", result)
