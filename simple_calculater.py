First_Value=eval(input("Enter first value-:"))
second_Value=eval(input("Enter second value-:"))
opr=input("Enter thee Opr-:")

if opr=="+":
    opr=First_Value+second_Value
    print(f'Answer is {opr}')
elif opr=="-":
    opr=First_Value-second_Value
    print(f'Answer is {opr}')
elif opr=="*":
    opr=First_Value*second_Value
    print(f'Answer is {opr}')
elif opr=="/":
    opr=First_Value/second_Value
    print(f'Answer is {opr}')

else:
    print("Invalid opr...")    
   
   
   
   

