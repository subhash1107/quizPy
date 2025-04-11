import random
from colorama import init, Fore, Style

# Initialising colorama so that we can use coloured output in terminal
init(autoreset=True)

# This function will read questions from the file and prepare a list of questions
def fetchQues(fileName):
    qs = []
    with open(fileName, "r") as f:
        for line in f:
            parts = line.strip().split(',')
            # Checking if the line has proper 6 parts (question + 4 options + correct answer)
            if len(parts) == 6:
                q = {
                    "ques": parts[0],         # Question text
                    "opts": parts[1:5],       # Options A to D
                    "ans": parts[5].strip().upper()  # Correct answer (converted to uppercase)
                }
                qs.append(q)
    return qs

# This function will ask one question at a time
def askQ(q, idx):
    print(f"\n{Fore.CYAN}Question {idx + 1}: {q['ques']}")
    # Printing all four options
    print(f"A. {q['opts'][0]}")
    print(f"B. {q['opts'][1]}")
    print(f"C. {q['opts'][2]}")
    print(f"D. {q['opts'][3]}")

    # Asking for user input until they give a valid input
    while True:
        userAns = input(f"{Style.BRIGHT}Your Answer (A/B/C/D): ").strip().upper()
        if userAns in ['A', 'B', 'C', 'D']:
            break
        else:
            print(f"{Fore.RED}Please enter a valid option: A, B, C, or D.")

    # Checking if the given answer is correct
    if userAns == q['ans']:
        print(f"{Fore.GREEN}Correct.")
        return True
    else:
        print(f"{Fore.RED}Incorrect. The correct answer is {q['ans']}.")
        return False

# This is the main function where quiz starts
def startQuiz():
    print(f"{Style.BRIGHT}{Fore.YELLOW}Welcome to the Quiz Application")
    print(f"{Fore.YELLOW}Instructions:")
    print("- Each question has four options.")
    print("- Enter A, B, C, or D as your answer.")
    input("\nPress Enter to begin...")  # Waiting for user to start

    qs = fetchQues("questions.txt")      # Loading all questions from file
    pickedQs = random.sample(qs, 10)     # Picking 10 random questions

    score = 0
    for i, q in enumerate(pickedQs):     # Looping through all selected questions
        if askQ(q, i):                   # Asking question and checking if correct
            score += 1

    # After all questions done, showing final score
    print(f"\n{Style.BRIGHT}{Fore.GREEN}Quiz Complete. Your Score: {score}/10")

    # Giving option to user to save their score
    name = input("Enter your name to save your score (leave blank to skip): ").strip()
    if name:
        with open("scores.txt", "a") as f:
            f.write(f"{name},{score}/10\n")
        print(f"{Fore.MAGENTA}Score saved successfully.")

# Starting the quiz
startQuiz()
