#random number

import random    
theNumber = random.randint(1,10)
print("Hello there :) Let's play. Can you guess the number on my mind?")
guessNumber = int(input("Give it a try, what number I am thinking about? "))


while guessNumber != theNumber:
    print("Nope, the number is different")
    if guessNumber > theNumber:
        print("The number is smaller than that")
    elif guessNumber < theNumber:
        print("The number is bigger than that")
    guessNumber = int(input("Try again "))

print("Amazing! You guessed the number! It is ",theNumber," indeed!")


#selected number
  
theNumber = 5
print("Hello there :) Let's play. Can you guess the number on my mind?")
guessNumber = int(input("Give it a try, what number I am thinking about? "))

while guessNumber != theNumber:
    print("Nope, the number is different")
    if guessNumber > theNumber:
        print("The number is smaller than that")
    elif guessNumber < theNumber:
        print("The number is bigger than that")
    guessNumber = int(input("Try again: "))

print("Amazing! You guessed the number! It is",theNumber,"indeed!")



