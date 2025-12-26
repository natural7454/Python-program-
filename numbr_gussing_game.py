import random

computer=random.randint(1,20)


Person=int(input("Enter The Your number-:"))
if computer==Person:
    print(f'Congratulations! You guessed {Person} and computer guessed {computer} it correctly')
elif computer<=Person:
    print(f'Computer number is {computer} and Your Number is {Person} Is Bigger')

elif(computer>=Person):
    print(f'Computer number is {computer} and Your Number is {Person} Is Low')

