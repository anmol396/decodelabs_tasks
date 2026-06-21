"""Rule-based chatbot for beginners.

This chatbot uses only simple Python control flow and predefined rules.
"""

from datetime import datetime


def print_startup_message():
    """Print the chatbot banner and startup instructions."""
    print("# =================================")
    print("RULE-BASED AI CHATBOT")
    print("Commands:")
    print()
    print("- Type 'help' -> Show commands")
    print("- Type 'menu' -> Show options")
    print("- Type 'exit' or 'bye' -> Close chatbot")
    print()
    print("# Question Count: 0")


def show_help():
    """Print the main command categories."""
    print("Available Commands:")
    print()
    print("- Greetings")
    print("- AI Questions")
    print("- Date/Time")
    print("- Math")
    print("- Jokes")
    print("- Exit")


def print_question_count(question_count):
    """Print the current question count after each answer."""
    print("Questions Asked:", question_count)


def print_limit_warning():
    """Tell the user they reached the 10-question limit."""
    print("---")
    print("You have asked 10 questions.")
    print("Type:")
    print()
    print("- continue -> Keep chatting")
    print("- exit -> Close chatbot")
    print("---")


def print_chat_summary(total_questions):
    """Print the closing summary before the chatbot exits."""
    print()
    print("# ====================")
    print("CHAT SUMMARY")
    print()
    print("# Total Questions Asked:", total_questions)
    print("Session Completed")
    print("Thank you for using RuleBot.")


def parse_number(number_text):
    """Convert text into a number, using integers first for exact results."""
    cleaned_text = number_text.strip()

    if cleaned_text == "":
        raise ValueError

    try:
        return int(cleaned_text)
    except ValueError:
        return float(cleaned_text)


def get_math_input(prompt_text):
    """Ask the user for a number and keep asking until the input is valid."""
    while True:
        try:
            # Convert the user's entry into a number for math commands.
            return parse_number(input(prompt_text))
        except ValueError:
            print("Bot: Please enter valid numbers.")


def get_clean_segment(segment_text):
    """Return the first meaningful token from a text segment."""
    cleaned_text = segment_text.strip()

    if cleaned_text == "":
        raise ValueError

    return cleaned_text.split()[0]


def calculate_inline_math(command, math_text):
    """Handle math expressions that are written in the same sentence."""
    cleaned_text = math_text.strip().replace(" ", "")

    try:
        if command == "square":
            number_text = get_clean_segment(cleaned_text)
            number = parse_number(number_text)
            return number * number

        elif command == "add":
            if "+" in cleaned_text:
                parts = cleaned_text.split("+")
            elif "and" in cleaned_text:
                parts = cleaned_text.split("and")
            else:
                parts = []

            if len(parts) == 2:
                first_number = parse_number(get_clean_segment(parts[0]))
                second_number = parse_number(get_clean_segment(parts[1]))
                return first_number + second_number

        elif command == "multiply":
            if "*" in cleaned_text:
                parts = cleaned_text.split("*")
            elif "and" in cleaned_text:
                parts = cleaned_text.split("and")
            else:
                parts = []

            if len(parts) == 2:
                first_number = parse_number(get_clean_segment(parts[0]))
                second_number = parse_number(get_clean_segment(parts[1]))
                return first_number * second_number

    except ValueError:
        print("Bot: Please enter valid numbers.")
        return None

    print("Bot: Please enter valid numbers.")
    return None


def handle_math_command(command, user_input):
    """Handle basic math commands using simple if-elif-else logic."""
    if command == "add":
        # Try to calculate an inline expression first.
        inline_text = user_input[user_input.find("add") + len("add"):]
        if inline_text.strip() != "":
            result = calculate_inline_math("add", inline_text)
            if result is not None:
                print("Bot:", result)
        else:
            # Ask for two numbers one by one if no inline math was given.
            first_number = get_math_input("Bot: Enter first number: ")
            second_number = get_math_input("Bot: Enter second number: ")
            print("Bot:", first_number + second_number)

    elif command == "multiply":
        # Try to calculate an inline expression first.
        inline_text = user_input[user_input.find("multiply") + len("multiply"):]
        if inline_text.strip() != "":
            result = calculate_inline_math("multiply", inline_text)
            if result is not None:
                print("Bot:", result)
        else:
            # Ask for two numbers one by one if no inline math was given.
            first_number = get_math_input("Bot: Enter first number: ")
            second_number = get_math_input("Bot: Enter second number: ")
            print("Bot:", first_number * second_number)

    elif command == "square":
        # Try to calculate an inline expression first.
        inline_text = user_input[user_input.find("square") + len("square"):]
        if inline_text.strip() != "":
            result = calculate_inline_math("square", inline_text)
            if result is not None:
                print("Bot:", result)
        else:
            # Ask for one number if no inline value was given.
            number = get_math_input("Bot: Enter a number: ")
            print("Bot:", number * number)


def normalize_input(user_input):
    """Make user input easier to match using simple keyword checks."""
    # Convert to lowercase and remove extra spaces
    cleaned_input = user_input.lower().strip()
    # Remove punctuation by replacing with spaces
    punctuation = [",", ".", "!", "?", ":", ";", "'", '"']

    for symbol in punctuation:
        cleaned_input = cleaned_input.replace(symbol, " ")

    # Convert multiple spaces into a single space
    cleaned_input = " ".join(cleaned_input.split())
    return cleaned_input


def contains_keyword(user_input, keyword):
    """Check whether a phrase appears in the user input."""
    return keyword in user_input


def contains_word(user_input, word):
    """Check whether a single word appears as its own token."""
    return word in user_input.split()


def get_response(user_input):
    """Return the chatbot response for supported text commands."""
    if contains_keyword(user_input, "close chat") or contains_keyword(user_input, "stop") or contains_keyword(user_input, "bye") or contains_keyword(user_input, "exit") or contains_keyword(user_input, "quit"):
        # End the loop immediately when the user wants to leave.
        print("Bot: Goodbye! Have a nice day.")
        return "exit"

    elif contains_word(user_input, "hi") or contains_word(user_input, "hello") or contains_word(user_input, "hey"):
        # Handle mixed greetings like "hi, how are you".
        if contains_keyword(user_input, "how are you"):
            print("Bot: Hello! I'm doing great.")
        elif contains_word(user_input, "hi"):
            print("Bot: Hello! Nice to meet you.")
        elif contains_word(user_input, "hello"):
            print("Bot: Hi there!")
        else:
            print("Bot: Hey! How can I help?")

    elif contains_keyword(user_input, "what is your name"):
        print("Bot: My name is RuleBot.")
    elif contains_keyword(user_input, "who are you"):
        print("Bot: I am a rule-based chatbot.")
    elif contains_keyword(user_input, "who made you"):
        print("Bot: I was created using Python.")
    elif contains_keyword(user_input, "how are you"):
        print("Bot: I'm doing great. Thanks for asking.")
    elif contains_keyword(user_input, "how is your day"):
        print("Bot: My day is great.")
    elif contains_keyword(user_input, "thank you"):
        print("Bot: You're welcome.")
    elif contains_keyword(user_input, "good morning"):
        print("Bot: Good morning.")
    elif contains_keyword(user_input, "good night"):
        print("Bot: Good night.")
    elif contains_keyword(user_input, "help") or contains_keyword(user_input, "menu") or contains_keyword(user_input, "commands"):
        show_help()
    elif contains_keyword(user_input, "what is python"):
        print("Bot: Python is a programming language.")
    elif contains_keyword(user_input, "what is ai"):
        print("Bot: AI (Artificial Intelligence) enables computers to simulate human intelligence and perform tasks like learning, decision-making, and problem-solving.")
    elif contains_keyword(user_input, "what is machine learning"):
        print("Bot: Machine Learning enables computers to learn from data.")
    elif contains_keyword(user_input, "tell me a joke"):
        print("Bot: Why do programmers hate nature? Too many bugs.")
    elif contains_keyword(user_input, "tell me a fact"):
        print("Bot: The first computer bug was an actual bug.")
    elif contains_keyword(user_input, "motivate me"):
        print("Bot: Keep learning and building projects.")
    elif contains_keyword(user_input, "what time is it"):
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot:", current_time)
    elif contains_keyword(user_input, "what is today's date"):
        current_date = datetime.now().strftime("%Y-%m-%d")
        print("Bot:", current_date)
    elif contains_keyword(user_input, "add"):
        handle_math_command("add", user_input)
    elif contains_keyword(user_input, "multiply"):
        handle_math_command("multiply", user_input)
    elif contains_keyword(user_input, "square"):
        handle_math_command("square", user_input)
    elif contains_keyword(user_input, "i am happy"):
        print("Bot: That's great to hear.")
    elif contains_keyword(user_input, "i am sad"):
        print("Bot: Hope things improve soon.")
    elif contains_keyword(user_input, "i am bored"):
        print("Bot: Try learning something new.")
    elif contains_keyword(user_input, "do you like me"):
        print("Bot: Of course 🙂")
    elif contains_keyword(user_input, "are you human"):
        print("Bot: No, I am a chatbot.")
    elif contains_keyword(user_input, "can you think"):
        print("Bot: I follow predefined rules.")
    else:
        print("Bot: Sorry, I don't understand. Type 'help' to see available commands.")
    return "answered"


def main():
    """Start the chatbot and keep it running until the user exits."""
    # Show a welcome message before starting the conversation loop.
    print_startup_message()

    # Keep talking to the user until an exit command is entered.
    total_questions = 0
    questions_since_reset = 0
    waiting_for_continue = False

    while True:
        user_input = normalize_input(input("User: "))

        if waiting_for_continue:
            if contains_keyword(user_input, "continue"):
                waiting_for_continue = False
                questions_since_reset = 0
            elif contains_keyword(user_input, "close chat") or contains_keyword(user_input, "stop") or contains_keyword(user_input, "bye") or contains_keyword(user_input, "exit") or contains_keyword(user_input, "quit"):
                print_chat_summary(total_questions)
                break
            else:
                print_limit_warning()
        else:
            response_status = get_response(user_input)

            if response_status == "exit":
                print_chat_summary(total_questions)
                break

            total_questions += 1
            questions_since_reset += 1
            print_question_count(total_questions)

            if questions_since_reset == 10:
                print_limit_warning()
                waiting_for_continue = True


if __name__ == "__main__":
    main()
