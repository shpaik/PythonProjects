print("\n--------------Create Voca Book--------------")
print("start with create your own quiz book!")
print("*press 'q' to take the quiz")
voca_input = open('vocabulary.txt', 'w')

while True:                                       # infinite loop
    # recieve Eng input
    english = input("Insert English voca: ")
    if english == "q":                              # exit when q pressed
        break

    # recieve Korean input
    korean = input("Insert meaning in your language: ")
    if korean =="q":                                # exit when q pressed
        break

    # Write at vocabulary.txt
    voca_input.write("%s: %s\n" % (english, korean))

# close file
voca_input.close()

print("\n-------------- Voca Quiz--------------")
print("press 'q' to take advanced quiz")

# open the file
voca_quiz = open('vocabulary.txt', 'r')

# read each line
for line in voca_quiz:
    # data collection
    data = line.strip().split(": ")
    english = data[0]
    korean = data[1]

    # provide Eng & take guess 
    guess = input("%s: " % (korean))

    # result
    if guess == english:
        print("Correct!\n")
    else:
        print("Unfortunately, the answer is %s.\n" % (english))

voca_quiz.close()

print("\n-------------- Random Quiz--------------")
print("press 'q' to quit")
voca_advanced = open('vocabulary.txt', 'r')
from random import randint

# create voca dictionary
voca = {}
for line in voca_advanced:              # read each line
     data = line.strip().split(": ")

     voca[data[1]] = data[0]             # pairing each voca


# create questions
while True:
    # make key in voca dic to list 
    keys = list(voca.keys())

    # randomly select Eng & meaning 
    i = randint(0, len(keys) - 1)
    korean = keys[i]
    english = voca[korean]

    # show quiz
    guess = input("%s: " % (korean))

    # resut
    if guess == 'q':                                            
        break
    elif guess == english:                                      
        print("Correct!")
    else:                                                       
        print("Unfortunately, the answer is %s." % (english))

# close file
voca_advanced.close()