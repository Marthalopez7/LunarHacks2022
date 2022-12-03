<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A Wish from the Earth</title>
    <link rel="stylesheet" href="https://use.typekit.net/style.css">
</head>
<body>
    <main>
        <h1>TEST YOUR KNOWLEDGE - Marine Pollution:</h1>
        <div class="python">
            <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
            <script defer src="https://pyscript.net/latest/pyscript.js"></script>
            <py-script>
                print("Welcome to Marine Pollution Trivia")
                print("When answering questions, please choose the answer that seems to be most accurate. Enter the corresponding letter for the choices, or indicate whether the statement is True or False.")
                print("\nEnter 0 at any time to exit.")
                
                # playAgain boolean to keep track of whether the user wants to play Again
                playAgain = True
                
                # =========CONSTANTS=================
                CORRECT = "You are correct!"
                INCORRECT = "You are incorrect!"
                
                # list constant for possible choices the user could input for multiple choice
                CHOICES = ["A", "B", "C", "D", "E", "0"]
                # list constant for possible things user could input for true or false
                TRUEORFALSE = ["false", "f", "true", "t", "0"]
                
                INVALIDANSWERABCD = "\nInvalid answer. Please enter either A, B, C, or D."
                INVALIDANSWERTF = "\nInvalid answer. Please indidcate whether [true] or [false] OR [t] or [f]."
                
                NUMBEROFQUESTIONS = 8
                SCORETRACKER = "Your score is"
                
                # below are the list constants for each question. the multiple choice question lists include: question, answer choices, and index of correct answer in the list in the last index (5). the true or false questions contain the question, true or false answer choices, and the index of the correct answer in the last index (3).
                # in this list "B" would be the correct answer since the last integer is 2
                Q1 = ["\nQuestion 1) How much plastic is dumped into the ocean per year?",
                    "A) 23 million tons", "B) 12 million tons", "C) 9 million tons", "D) 17 million tons", "E) 22 million tons", 2]
                
                Q2 = ["\nQuestion 2) What happens to ocean when gasoline is used?", "A) It loses volume.", "B) Sea levels rise.",
                    "C) It becomes more acidic.", "D) People can't go to beaches.", "E) Fishermen lose their jobs.", 3]
                
                Q3 = ["\nQuestion 3) How does plastic affect dolphins?", "A) They get lost in the plastic.", "B) They are poisoned from the plastic.",
                    "C) They get stuck in trash webs, and can choke from it.", "D) They can't reproduce any more.", "E) They get plastic stuck on their body, weighing them down.", 3]
                
                Q4 = ["\nQuestion 4) True or False: Almost 1000 species of marine animals get impacted by ocean pollution.", "true", "false", 1]
                
                Q5 = ["\nQuestion 5) How many years does it take for plastic to degrade?", "A) 600-1200 years",
                    "B) 200-500 years", "C) 1000-2000 years", "D) 100-300 years", "E) 500-1000 years", 5]
                
                Q6 = ["\nQuestion 6) True or False: The United States is the country that causes the most marine pollution in the world.", "true", "false", 2]
                
                Q7 = ["\nQuestion 7) How many marine animals die each year from plastic debris?",
                    "A) 1 million", "B) 2 million", "C) 3 million", "D) 4 million", "E) 5 million", 1]
                
                Q8 = ["\nQuestion 7) What is the number one pollutant of oceans?", "A) Eutrophication",
                    "B) Ocean acificication", "C) Toxins", "D) Noise", "E) Plastic debris", 2]
                
                # ==================game starts=================================
                while (playAgain == True):
                    # score variable to keep track of score
                    score = 0
                
                    # empty list to keep track of which questions user got CORRECT
                    correctAnswers = []
                
                    # ================question 1==================
                    # prints question 1, answer choices, and then prompts for the user answer
                    print(Q1[0])
                    for i in Q1[1:6]:
                        print(i)
                    answer = input("\nYour answer: ")
                
                    # this loop makes sure that the users answer is one of the letters for the multiple choice question
                    while (answer.upper() not in CHOICES):
                        print(INVALIDANSWERABCD)
                        answer = input("\nYour answer: ")
                
                    # after making sure the input is valid, the program will check if the user wants to exit
                    if (answer == "0"):
                        playAgain = False
                        continue  # continue allows the code to return to the beginning of the while loop - therefore, because playAgain is false, and it returns to the beginning, the game will end
                
                    # then, if the user DOES NOT want to exit by pressing 0, it will finally check if it corresponds to the letter of the correct answer.
                    # how the code works for checking the right answer:
                    # Q1[5] = 2, which is the index NUMBER for the correct answer. This means Q1[Q1[5]] is equal to Q1[2], which is actual correct answer
                    elif (answer.upper() == Q1[Q1[-1]][0]):
                        print(CORRECT)  # prints the already prepared message for "CORRECT"
                        score += 1
                        # this will just append the question number to the empty list "correctAnswers" if the user got the question correct
                        correctAnswers.append("1")
                        # prints a prepared message and the score
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)  # same, but there is a message for "INCORRECT"
                        print("\n" + SCORETRACKER, score)
                
                    # ===================question 2=====================
                    print(Q2[0])
                    for i in Q2[1:6]:
                        print(i)
                    answer = input("\nYour answer: ")
                
                    while (answer.upper() not in CHOICES):
                        print(INVALIDANSWERABCD)
                        answer = input("\nYour answer: ")
                
                    if (answer == "0"):
                        playAgain = False
                        continue
                
                    elif (answer.upper() == Q2[Q2[-1]][0]):
                        print(CORRECT)
                        score += 1
                        correctAnswers.append("2")
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)
                        print("\n" + SCORETRACKER, score)
                
                    # ===============question 3====================
                    print(Q3[0])
                    for i in Q3[1:6]:
                        print(i)
                    answer = input("\nYour answer: ")
                
                    while (answer.upper() not in CHOICES):
                        print(INVALIDANSWERABCD)
                        answer = input("\nYour answer: ")
                
                    if (answer == "0"):
                        playAgain = False
                        continue
                
                    elif (answer.upper() == Q3[Q3[-1]][0]):
                        print(CORRECT)
                        score += 1
                        correctAnswers.append("3")
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)
                        print("\n" + SCORETRACKER, score)
                
                    # ===========question 4====================
                    print(Q4[0])
                    answer = input("\nYour answer: ")
                
                    # invalid answer if it is not in the list of choices TRUEORFALSE
                    while (answer.lower() not in TRUEORFALSE):
                        print(INVALIDANSWERTF)
                        answer = input("\nYour answer: ")
                
                    if (answer == "0"):
                        playAgain = False
                        continue
                
                    # because it is a true or false question, the indexing and conditions are a bit different
                    # in this case, Q4[Q4[3]] refers to the correct answer (which would be "false") and Q4[Q4[3]][0] refers to the first letter in the correct answer (which would be "f") so the program would accept both possible answers entered by the user
                    if (answer.lower() == Q4[Q4[3]]) or (answer.lower() == Q4[Q4[-1]][0]):
                        print(CORRECT)
                        score += 1
                        correctAnswers.append("4")
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)
                        print("\n" + SCORETRACKER, score)
                
                    # ===============question 5====================
                    print(Q5[0])
                    for i in Q5[1:6]:
                        print(i)
                    answer = input("\nYour answer: ")
                
                    while (answer.upper() not in CHOICES):
                        print(INVALIDANSWERABCD)
                        answer = input("\nYour answer: ")
                
                    if (answer == "0"):
                        playAgain = False
                        continue
                
                    elif (answer.upper() == Q5[Q5[-1]][0]):
                        print(CORRECT)
                        score += 1
                        correctAnswers.append("5")
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)
                        print("\n" + SCORETRACKER, score)
                
                    # ================question 6=================
                    print(Q6[0])
                    answer = input("\nYour answer: ")
                
                    while (answer.lower() not in TRUEORFALSE):
                        print(INVALIDANSWERTF)
                        answer = input("\nYour answer: ")
                
                    if (answer == "0"):
                        playAgain = False
                        continue
                
                    if (answer.lower() == Q6[Q6[3]]) or (answer.lower() == Q6[Q6[-1]][0]):
                        print(CORRECT)
                        score += 1
                        correctAnswers.append("6")
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)
                        print("\n" + SCORETRACKER, score)
                
                    # ===============question 7====================
                    print(Q7[0])
                    for i in Q7[1:6]:
                        print(i)
                    answer = input("\nYour answer: ")
                
                    while (answer.upper() not in CHOICES):
                        print(INVALIDANSWERABCD)
                        answer = input("\nYour answer: ")
                
                    if (answer == "0"):
                        playAgain = False
                        continue
                
                    elif (answer.upper() == Q7[Q7[-1]][0]):
                        print(CORRECT)
                        score += 1
                        correctAnswers.append("7")
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)
                        print("\n" + SCORETRACKER, score)
                
                    # ===============question 8====================
                    print(Q8[0])
                    for i in Q8[1:6]:
                        print(i)
                    answer = input("\nYour answer: ")
                
                    while (answer.upper() not in CHOICES):
                        print(INVALIDANSWERABCD)
                        answer = input("\nYour answer: ")
                
                    if (answer == "0"):
                        playAgain = False
                        continue
                
                    elif (answer.upper() == Q8[Q8[-1]][0]):
                        print(CORRECT)
                        score += 1
                        correctAnswers.append("8")
                        print("\n" + SCORETRACKER, score)
                    else:
                        print(INCORRECT)
                        print("\n" + SCORETRACKER, score)
                
                    # =================end of game code=========================
                    print(f"\nFinal score: {score} out of {NUMBEROFQUESTIONS}")
                
                    # if "correctAnswers" is still an empty list, the user will have gotten none of the questions right, the program will proceed to announce this
                    if (correctAnswers == []):
                        print("You got no questions correct :( Better luck next time!")
                
                    elif (len(correctAnswers) == NUMBEROFQUESTIONS):
                        print("Congratulations! You're a marine knowledge expert!")
                
                    # otherwise, the program will specify which questions the user got correct
                    else:
                        # this part of the program makes the "printCorrectAnswers" variable so that it can use the ".join()" function to put all the items in the list together with a comma in between. then, to make sure the last item in the list is separate with "and" instead of a comma, we take all the items in the list other than the last one (index -1), add "and", then add the last item
                        printCorrectAnswers = ", ".join(correctAnswers)
                        if (len(printCorrectAnswers) > 1):
                            printCorrectAnswers = printCorrectAnswers[:-
                                                                    1] + "and " + printCorrectAnswers[-1]
                
                        print(f"You got questions {printCorrectAnswers} correct.")
                
                    # all the questions have been asked so the program will ask the user whether they want to play again
                    askPlayAgain = input(
                        "\nWould you like to play again? Enter 0 to exit or anything else to play again: ")
                    if (askPlayAgain == "0"):
                        playAgain = False  # when the user enters 0, the loop ends - game will end
                        # anything else the user inputs will cause the loop to restart and the game will reset
                
                # when the game ends, there is a thank you message
                print("\nThank you for playing Marine Pollution Trivia.")
            </py-script>
        </div>
    </main>
</body>
</html>
