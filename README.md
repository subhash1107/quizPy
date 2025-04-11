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
- Saved scores in json file if existing user then save inside same user container otherwise create other.
- Uses `colorama` for clean colored output in terminal

---
## Installation

### 1. Check if Python is installed

Open a terminal or command prompt and run:

```bash
py --version
```
### 2. If Python is not installed, download it from the official site:
- Click on the given link and follow the instructions given on site to install
https://www.python.org/downloads/

### 3. Install Required Package (colorama)
```bash
py -m pip install colorama
```
---


## How to Run

1. Make sure you have the following files in the same directory:
   - `quiz.py` — the main Python script
   - `questions.txt` — contains the quiz questions

2. Open a terminal or command prompt in that folder.

3. Run the app using this command:

```bash
py quiz.py
```
Follow the on-screen instructions to play the quiz and optionally save your score.

---

## Note on questions.txt Format

Each question must follow this format:
```txt
Question,Option A,Option B,Option C,Option D,Correct Option (A/B/C/D)
```
Example
```txt
What is the capital of France?,Berlin,Madrid,Paris,Rome,C
```
Make sure there are no extra spaces or missing fields.

---
That's it! You're all set to use the Console Quiz App.



