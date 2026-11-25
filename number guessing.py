import random
number=random.randint(1,100)
attempts=0
print("Welcome to the Number guessing Game!!")
print("Guess a Number between 1 to 100")

while True:
    guess=int(input("Your guess:"))
    attempts +=1

    if guess < number:
        print("Too low! Try Again.")
    elif guess > number:
        print("Too high! Try Again.")
    else:
        print(f"Correct! The number was {number}.")
        print(f"Attempts:{attempts}.")
        break
        
