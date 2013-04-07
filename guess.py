#ex01 from first week of class at Hackbright

from random import randint
prompt = (">> ")

print "Howdy, what's your name?"
name = raw_input(prompt)
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
#number_submitted = int(raw_input(prompt))
num = randint(1,101)
print num

guess = 0

#tried this with a for loop but it didn't work
#for num in number

while True:

    guess += 1
    number_submitted = int(raw_input(prompt))
    if num > number_submitted:
        print "Your guess is too low. Try again."
        #number_submitted = int(raw_input(prompt))
    elif num < number_submitted:
        print "Your guess is too high. Try again."
        #number_submitted = int(raw_input(prompt))
    else:
        print "%s, you guessed the answer in %r tries." % (name, guess)
        break