marks = int(input("Enter Your Marks : "))

if(marks <= 100 and marks >=90):
    grade = "EX"
elif(marks <= 89 and marks >=80):
    grade = "A"
elif(marks <= 79 and marks >=70):
    grade = "B"
elif(marks <= 69 and marks >=60):
    grade = "C"
elif(marks <= 59 and marks >=50):
    grade = "D"
elif(marks <= 49 and marks >=40):
    grade = "E"
else:
    grade = "F"
print(grade)