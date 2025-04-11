import random
from colorama import init, Fore, Style

init(autoreset=True)

def fetchQues(fileName):
    qs = []
    with open(fileName, "r") as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 6:
                q = {
                    "ques": parts[0],
                    "opts": parts[1:5],
                    "ans": parts[5].strip().upper()
                }
                qs.append(q)
    return qs

def askQ(q, idx):
    print(f"\n{Fore.CYAN}Question {idx + 1}: {q['ques']}")
    print(f"A. {q['opts'][0]}")
    print(f"B. {q['opts'][1]}")
    print(f"C. {q['opts'][2]}")
    print(f"D. {q['opts'][3]}")

    while True:
        userAns = input(f"{Style.BRIGHT}Your Answer (A/B/C/D): ").strip().upper()
        if userAns in ['A', 'B', 'C', 'D']:
            break
        else:
            print(f"{Fore.RED}Please enter a valid option: A, B, C, or D.")

    if userAns == q['ans']:
        print(f"{Fore.GREEN}Correct.")
        return True
    else:
        print(f"{Fore.RED}Incorrect. The correct answer is {q['ans']}.")
        return False

def startQuiz():
    print(f"{Style.BRIGHT}{Fore.YELLOW}Welcome to the Quiz Application")
    print(f"{Fore.YELLOW}Instructions:")
    print("- Each question has four options.")
    print("- Enter A, B, C, or D as your answer.")
    input("\nPress Enter to begin...")

    qs = fetchQues("questions.txt")
    pickedQs = random.sample(qs, 10)

    score = 0
    for i, q in enumerate(pickedQs):
        if askQ(q, i):
            score += 1

    print(f"\n{Style.BRIGHT}{Fore.GREEN}Quiz Complete. Your Score: {score}/10")

    name = input("Enter your name to save your score (leave blank to skip): ").strip()
    if name:
        with open("scores.txt", "a") as f:
            f.write(f"{name},{score}/10\n")
        print(f"{Fore.MAGENTA}Score saved successfully.")

# Start the quiz
startQuiz()
