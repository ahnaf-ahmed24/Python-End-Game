a1 = int(input("Enter Number  1 : "))
a2 = int(input("Enter Number  2 : "))
a3 = int(input("Enter Number  3 : "))
a4 = int(input("Enter Number  4 : "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is 1 : ",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is 2 : ",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is 1 : ",a3)
else:
    print("Greatest number is 4 : ",a4)