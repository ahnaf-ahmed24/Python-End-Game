n = int(input("Enter a number : "))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prinme")
        break

else:
    print("Number is not Prime")