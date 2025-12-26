num = int(input("Enter the number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("This is Not a Prime Number")
            break
    else:
        print("This IS a Prime Number")
else:
    print("This is NOT a Prime Number")

