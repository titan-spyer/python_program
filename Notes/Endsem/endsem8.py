student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95,
    "Fiona": 81
}
uinp = input("Enter name to check in list: ")
for name in student_scores:
    if uinp == name:
        print(student_scores[name])