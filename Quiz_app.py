
# Quiz App
""" Start Quiz,
ask questiomn,
get user answer,
check answer,
update score,
next question,
show final score,
ask to restart """

# get user name and set score to 0, so uisng dictionay for the quesion and answer
name = input("Enter your name: ")
score = 0

# use dictionary for the question and answer
ask_question = {
    "what is 2 + 2? ": "4",
    "how old are you: " : "20",
    "python is a programming......." : "Language"
    }

for question, answer in ask_question.items(): # using key as the question while using the value as the answer
    user_answer = input(question + " ")

    if user_answer.lower() == answer.lower(): # to convert any answer written in any style to lower case in order to avoid error
        print("Correct!")
        score += 1 # use to count value of total question gotten
    else:
        print("Wrong!")
print(f"Your final score is {score}")