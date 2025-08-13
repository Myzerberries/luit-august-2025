import random

roll = random.randint(1,6)

print ("Your random number is: " + str(roll))

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print ("Chicken din din! It's " + str(roll))

else:
    print ("Better luck next time champ. It's " + str(roll))