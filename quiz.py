import random
import json
import os
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init(autoreset=True)

# Load questions from file
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

# Ask one question with validation

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

# Save score to a JSON file with timestamp
def saveScore(name, score):
    filePath = "scores.json"
    data = {}

    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            data = json.load(f)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    newEntry = {"score": f"{score}/10", "time": now}

    if name in data:
        data[name].append(newEntry)
    else:
        data[name] = [newEntry]

    with open(filePath, "w") as f:
        json.dump(data, f, indent=4)

    print(f"{Fore.MAGENTA}Score saved successfully with timestamp.")

# Main quiz function
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
        saveScore(name, score)

# Start quiz
startQuiz()
