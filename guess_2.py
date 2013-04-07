from random import randrange

random_number = randrange(1, 10)
count = 0

while count < 3:
    guess = int(raw_input("You have three tries to guess my number. Enter a guess: "))
    count = count +1
    if guess == random_number:
        print ("You win!")
        break
else:
    print ("You lose.")