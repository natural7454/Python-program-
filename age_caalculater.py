Age=int(input("Enter the Age-:"))

if Age<=17:
    print("This Is Child")
elif Age>=18 and Age<=29:
    print("This is Young Men")
elif(Age>=30) and Age<=44:
    print("This is Adult man")
elif(Age>=45) and Age<=70:
    print("This is old man")
else:
    print("This is older")
    
