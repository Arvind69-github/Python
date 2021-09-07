marks: int = int(input("enter  marks: "))
total_marks: int = marks
if total_marks > 45:
    print("A grade")
elif total_marks <= 45 & total_marks > 30:
    print("B grade")
elif total_marks > 20 & total_marks <= 30:
    print("C grade")
else:
    print("Fail")