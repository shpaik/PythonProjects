# -*- coding: utf-8 -*-
from random import randint

# pick 3 numbers
def generate_numbers():
    answer = []

    # loop until get 3 different number
    while len(answer) <= 2:
        rand_num = randint(0, 9)
        if rand_num not in answer:
            answer.append(rand_num)
        else:                           
            continue

    return answer

# User guess
ANSWER = generate_numbers()
print("In this game, you guess what 3 numbers I picked between 0-9, exclusive. I will give you hint for every attempt.")
print("S means you correctly guess the number and spot")
print("B means you correctly guess the number but not the spot \n let's go!)

# variables
strike = 0      
ball = 0        
tries = 0       

while strike < 3:
    guess = []              # reset variable

# receive 3 inputs
    while len(guess) <= 2:
        guess_num = int(input("pick number %d: " % (len(guess) + 1)))

        # validate out of range
        if guess_num > 9 or guess_num < 0:
            print("범위를 벗어나는 수입니다. 다시 입력해주세요")
        # validate duplicated
        elif guess_num in guess:
            print("중복되는 수 입니다. 다시 입력해주세요")
        # right
        else:
            guess.append(guess_num)

# B/S Test
    testing_index = 0
    strike = 0
    ball = 0

    while testing_index <= 2:
        if guess[testing_index] == ANSWER[testing_index]:
            strike += 1
        elif guess[testing_index] in ANSWER:
            ball += 1
        testing_index += 1

    print("%dS %dB\n" % (strike, ball))

    tries += 1

# Msg
print("Congraturation! You correctly get three numbers and spots for %d attempt" % (tries))
