# The `questions` tuple is storing a series of questions related to different topics. Each question is
# a string that ends with a colon and a question mark. These questions are related to various subjects
# such as the periodic table, animal facts, atmospheric gases, human anatomy, and planets in the solar
# system.
questions = ("How many elements are there in periodic table? : ",
            "Which element lays the largest eggs? : ",
            "which is the most abundant gas in the Earth's atmosphere? :",
            "How many bones are there in the human body? : ",
            "Which planet in the solar system is the hottest? : ")
# The `options` tuple is storing multiple tuples, each containing four strings representing the answer
# choices for the corresponding question in the `questions` tuple. Each inner tuple represents the
# answer choices for a specific question. The answer choices are presented in a multiple-choice format
# with options A, B, C, and D followed by the actual answer text. This structure allows the user to
# select one of the options as their answer when responding to the questions during the quiz.


options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. Hydrogen"),
           ("A. 207","B. 206","C. 208","D. 210"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))

# The code snippet `answers = ("C","D","A","B","B")` is defining a tuple named `answers` that stores
# the correct answers to the quiz questions. Each element in the `answers` tuple corresponds to the
# correct answer for a specific question in the `questions` tuple.
answers = ("C","D","A","B","B")
guesses = []
score = 0
question_number = 0


# The code snippet you provided is a Python script that conducts a quiz based on the questions, answer
# choices, and correct answers provided in the `questions`, `options`, and `answers` tuples,
# respectively.
for question in questions:
  print("------------------------------")
  print(question)
  for option in options[question_number]:
    print(option)
    
  guess = input("Enter (A,B,C,D): ").upper()
  guesses.append(guess)
    
  if guess == answers[question_number]:
      score += 1
      print("CORRECT")
  else:
      print("INCORRECT")
      print(f"{answers[question_number]} is the correct answer")
  question_number += 1

# The code snippet you provided is responsible for displaying the final result of the quiz after all
# the questions have been answered. It prints out a section titled "RESULT" with a horizontal line
# above and below it for visual separation.
# the questions have been answered. Here's a breakdown of what it does:

print("--------------------------")
print("         RESULT           ")
print("--------------------------")

print("answers: ",end=" ")
for answer in answers:
  print(answer, end=" ")
print()


print("guesses: ",end=" ")
for guess in guesses:
  print(guess, end=" ")
print()

# The line `print(f"your total score is : {score}")` is using an f-string in Python to dynamically
# insert the value of the `score` variable into the printed string.
# insert the value of the `score` variable into the string that is being printed.
print(f"your totoal score is : {score}")