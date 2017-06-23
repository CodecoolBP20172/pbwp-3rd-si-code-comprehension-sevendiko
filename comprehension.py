import random # import random module

guessesTaken = 0 # global variable, counting how many guesses taken 

print('Hello! What is your name?') # print out the text between the parentheses
myName = input() # user input assigned to a global variable

number = random.randint(1, 20) # generate a random number between 1, 20 and save it in a global variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # print out the text between the parentheses

while guessesTaken < 6: # the code below this line will be executed til' the variable value less than 6
    print('Take a guess.') # print..
    guess = input() # user input assigned to a local variable
    guess = int(guess) # this line convert the user input (guess) to integer

    guessesTaken += 1   # adding one to this variable, each time when the user guesses

    if guess < number:  
        print('Your guess is too low.') # print out the text between parentheses if guess less than number

    if guess > number:
        print('Your guess is too high.') # print out the text between parentheses if guess more than number

    if guess == number: # if guess matching with the actual number, the while loop break
        break

if guess == number: # examination to find out if guess equals number
    guessesTaken = str(guessesTaken) # this line convert the variable value to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') # print out...

if guess != number: # examination to find out if guess not equals number
    number = str(number) # this line convert the variable value to a string
    print('Nope. The number I was thinking of was ' + number) # print out


