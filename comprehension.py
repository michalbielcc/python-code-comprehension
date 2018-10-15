import random                                                             # import module "random"

guesses_taken = 0                                                         #create variable called "guesses_taken" with integer value of 0

print('Hello! What is your name?')                                        #print string"
myName = input()                                                          #take user input and store it as variable called "myName"

number = random.randint(1, 20)                                            #generate random integer between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')#pirnt string with user input a aprt of said string 

while guesses_taken < 6:                                                  #create loop working untiill guesses_taken reaches value of 6
    print('Take a guess.')                                                #print string
    guess = input()                                                       #take user input and asign it to variable called "guess"
    guess = int(guess)                                                    #convert user input into a string
                                                                          
    guesses_taken += 1                                                    #increase guesses_taken variable by 1

    if guess < number:                                                    #if guess value is lower than number value
        print('Your guess is too low.')                                   #print string

    if guess > number:                                                    #if guess value is higher than number value
        print('Your guess is too high.')                                  #print string

    if guess == number:                                                   #if guess value equals number value
        break                                                             #stop loop

if guess == number:                                                       # if guess value equals number value
    guesses_taken = str(guesses_taken)                                    #convert vlue of guesses_take into a string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!')#print string containing myName and guesses_taken

if guess != number:                                                       #if guess value does not equal number value
    number = str(number)                                                  #convert number vaalue into a sring
    print('Nope. The number I was thinking of was ' + number)             #print string containing number
