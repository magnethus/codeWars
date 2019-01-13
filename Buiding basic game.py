secret_word = "giraffe"
guess = ""
count = 0
number_Guess = 3
out_of_Guess = False

while guess != secret_word and not(out_of_Guess):
    if count < number_Guess:
        guess = raw_input("Enter guess: ")
        count += 1
    else:
        out_of_Guess = True
if out_of_Guess:
    print("Sorry, you are out of guess, Try Again!")
else:
    print("You win")