import random
import json
import os
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init(autoreset=True)

# Function to load questions from a given file
# Each line in the file should have: question,optA,optB,optC,optD,correctOption
# Returns a list of question dictionaries

def fetchQues(fileName):
    qs = []
    with open(fileName, "r") as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 6:
                q = {
                    "ques": parts[0],             # The question text
                    "opts": parts[1:5],           # Options A to D
                    "ans": parts[5].strip().upper()  # Correct answer (uppercase)
                }
                qs.append(q)
    return qs

# Function to ask one question to the user
# Displays the question, gets input, and returns True/False depending on correctness

def askQ(q, idx):
    print(f"\n{Fore.CYAN}Question {idx + 1}: {q['ques']}")
    print(f"A. {q['opts'][0]}")
    print(f"B. {q['opts'][1]}")
    print(f"C. {q['opts'][2]}")
    print(f"D. {q['opts'][3]}")

    # Keep prompting until user provides valid input (A-D)
    while True:
        userAns = input(f"{Style.BRIGHT}Your Answer (A/B/C/D): ").strip().upper()
        if userAns in ['A', 'B', 'C', 'D']:
            break
        else:
            print(f"{Fore.RED}Please enter a valid option: A, B, C, or D.")

    # Check and return whether user's answer is correct
    if userAns == q['ans']:
        print(f"{Fore.GREEN}Correct.")
        return True
    else:
        print(f"{Fore.RED}Incorrect. The correct answer is {q['ans']}.")
        return False

# Function to save user's score into a JSON file with timestamp
# Appends new score to existing user's history or creates a new entry

def saveScore(name, score):
    filePath = "scores.json"
    data = {}

    # Load existing data if the file exists
    if os.path.exists(filePath):
        with open(filePath, "r") as f:
            data = json.load(f)

    # Prepare a new score entry with current timestamp
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    newEntry = {"score": f"{score}/10", "time": now}

    # Add score to existing user or create new user entry
    if name in data:
        data[name].append(newEntry)
    else:
        data[name] = [newEntry]

    # Write updated data back to file
    with open(filePath, "w") as f:
        json.dump(data, f, indent=4)

    print(f"{Fore.MAGENTA}Score saved successfully with timestamp.")

# Main function to run the quiz
# Loads questions, asks 10 random ones, and saves the final score

def startQuiz():
    print(f"{Style.BRIGHT}{Fore.YELLOW}Welcome to the Quiz Application")
    print(f"{Fore.YELLOW}Instructions:")
    print("- Each question has four options.")
    print("- Enter A, B, C, or D as your answer.")
    input("\nPress Enter to begin...")

    # Load and shuffle questions
    qs = fetchQues("questions.txt")
    pickedQs = random.sample(qs, 10)

    # Run quiz loop and calculate score
    score = 0
    for i, q in enumerate(pickedQs):
        if askQ(q, i):
            score += 1

    print(f"\n{Style.BRIGHT}{Fore.GREEN}Quiz Complete. Your Score: {score}/10")

    # Ask user to save score optionally
    name = input("Enter your name to save your score (leave blank to skip): ").strip()
    if name:
        saveScore(name, score)

# Start the quiz by calling main function
startQuiz()