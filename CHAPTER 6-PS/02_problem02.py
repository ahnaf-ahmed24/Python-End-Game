marks1 = int(input("Enter your Number 1 : "))
marks2 = int(input("Enter your Number 2 : "))
marks3 = int(input("Enter your Number 3 : "))

# Check for total percentage 
total_percentage = (100*(marks1 + marks2 +marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed. your percentage : ",total_percentage,"%")
else:
    print("you failed, try again next year. Your percentage : ", total_percentage,"%")