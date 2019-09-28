import random
x=random.randint(1,5)
y=1
while y==1:
    b = int(input("Enter a number:"))
    if(b==x):
        print("You won the lottery")
        y=0
    else:
        print("try again")
        y=1
