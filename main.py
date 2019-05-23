secret = 8
guess = int(input("Guess the secret number from 1 to 10: "))
if secret == guess:
    print("Congratulations, the secret number is " + str(secret) + "!")
else:
    print("Sorry, you are wrong!")