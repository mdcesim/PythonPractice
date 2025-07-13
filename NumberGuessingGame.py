import random

random_input = random.randrange(1,21)
print("You have only 5 guesses..")
user_input = int(input("Guess a number between 1-20 \n"))
difference = abs(user_input - random_input)
count = 1

while user_input != random_input and count < 5:
    difference = abs(user_input - random_input)
    
    if difference > 15:
        print("Too far")
    elif 10 < difference <= 15:
        print("far")
    elif 5 < difference <= 10:
        print ("Close")
    elif 1 < difference <= 5:
        print("Too Close")

    count = count +1
    if count == 5:
        print(f"No more tries. You lose. The correct number was {random_input}")
        break
    user_input = int(input("Guess again\n"))

if user_input == random_input:
        print(f"Congratolations. You won..\n The number is {random_input}")