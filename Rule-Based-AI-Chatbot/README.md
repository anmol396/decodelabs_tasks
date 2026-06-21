# Rule-Based-AI-Chatbot

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)](https://www.python.org/)

</div>

A simple Python chatbot that responds to predefined user inputs using **rule-based logic** and **conditional statements**.

This project demonstrates chatbot fundamentals without machine learning by using `if-elif-else`, loops, and basic input processing.

---

## Project Overview

The chatbot accepts user input, matches predefined commands, and returns responses based on rules.

It supports:

* Greetings and conversations
* AI and Python-related questions
* Fun interactions
* Date and time responses
* Simple calculations
* Exit commands

---

## Features

* Rule-based chatbot implementation
* Continuous conversation using loops
* Input normalization using `lower()`
* Multiple response categories
* Beginner-friendly structure
* No external libraries required

---

## Chatbot Workflow

```text
Start
 ↓
Display Welcome Message
 ↓
Accept User Input
 ↓
Convert Input to Lowercase
 ↓
Match Rules (if-elif-else)
 ↓
Generate Response
 ↓
Continue / Exit
```

---

## Supported Commands

| Category     | Examples                       |
| ------------ | ------------------------------ |
| Greetings    | hi, hello, hey                 |
| Introduction | who are you, what is your name |
| Conversation | how are you, thank you         |
| Learning     | what is python, what is ai     |
| Fun          | joke, motivate me              |
| Date & Time  | current date, current time     |
| Math         | add, multiply, square          |
| Mood         | i am happy, i am sad           |
| Exit         | exit, quit, bye                |

---

## Tech Stack

| Component       | Technology   |
| --------------- | ------------ |
| Language        | Python       |
| Built-in Module | datetime     |
| Logic           | if-elif-else |
| Execution       | while loop   |

---

## Project Structure

```text
Rule-Based-AI-Chatbot/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/anmol396/Rule-Based-AI-Chatbot.git
```

Move into the folder:

```bash
cd Rule-Based-AI-Chatbot
```

Install dependencies (if required):

```bash
pip install -r requirements.txt
```

Run the chatbot:

```bash
python chatbot.py
```

---

## Example Interaction

```text
Bot → Welcome! Type 'exit' anytime.

User → hi
Bot → Hello! Nice to meet you.

User → what is ai
Bot → AI stands for Artificial Intelligence.

User → bye
Bot → Goodbye! Have a nice day.
```

---

## Learning Outcomes

After completing this project:

* Build a console-based chatbot
* Work with conditions and loops
* Process user input
* Understand rule-based AI concepts
* Organize Python projects

---

## Future Improvements

* GUI using Tkinter
* Voice interaction
* NLP-based chatbot
* Web deployment

---

Developed as part of **Project 1 – Rule-Based AI Chatbot**
