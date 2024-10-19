
import random
n=random.randrange(1,10)
guess = int(input("Enter any Number:"))
while n!=guess:
    if guess <n:
        print ("too low")
        guess =int (input("Enter N umber Again:"))
    elif guess > n :
        print ("too high!")
        guess=int (input ("Enter Number Again:"))
    else :
        break
print ("You guessed it Right!!")