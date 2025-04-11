# Console Quiz App

A terminal-based quiz game built in Python. It loads multiple-choice questions from a file, presents 10 randomly selected questions, and tracks the user’s score. There's also an option to save the score with a name and timestamp.

---

## Features

- Reads questions from `questions.txt`
- Randomly selects 10 unique questions for each session
- Validates input (only A, B, C, or D are accepted)
- Immediate feedback after each answer
- Displays final score out of 10
- Option to save the score with username and date-time
- Uses `colorama` for clean colored output in terminal

---

## How to Run

1. Make sure you have the following files in the same directory:
   - `quiz.py` — the main Python script
   - `questions.txt` — contains the quiz questions

2. Open a terminal or command prompt in that folder.

3. Run the app using this command:

```bash
py quiz.py
