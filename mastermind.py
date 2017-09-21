import os, sys, random
from datetime import datetime

def generate_answer(difficulty="Medium"):
    if difficulty == "Hard":
        endRange = 99999
    elif difficulty == "Easy":
        endRange = 999
    else:
        endRange =9999
    number=random.randrange(0,endRange)
    return str(number).zfill(4)

def take_guess(attempts, difficulty):
    if difficulty=="Easy":
        length = 3
    elif difficulty=="Medium":
        length = 4
    elif difficulty=="Hard":
        length = 5
    valid=False
    while not valid:
        guess = raw_input(str(attempts)+'> ')
    
        try:
            int(guess)
            if len(guess) == length:
                valid=True
                return str(guess)
            else:
                print_input_error(length)
        except(ValueError):
            print_input_error(length)

def print_input_error(length):
    print "Please enter a "+str(length)+" digit number."
    print "Use leading zeroes if necessary"

def compare_answer_to_guess(answer, guess):
    correct=""
    for i in range(4):
        if answer[i]==guess[i]:
            correct+="*"
    return correct

def main(argv):
    solved=False
    print "----Mastermind----"
    print "Guess the numbers in as few tries as possible"
    try:
        difficulty = argv[0]
    except:
        difficulty = "Medium"
    if difficulty=="Hard" or difficulty=="Medium":
        answer=generate_answer(difficulty)
    else:
        answer=generate_answer()
    attempts=1
    while not solved:
        guess = take_guess(attempts, difficulty)
        correct = compare_answer_to_guess(answer, guess)
        print correct
        if correct == "****":
            print "Well done... That took you ["+str(attempts)+"] attempts!"
            solved=True
        attempts+=1
    
if __name__ == "__main__":
     sys.exit(main(sys.argv[1:]))