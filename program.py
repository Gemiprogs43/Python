# import openai;

# openai.api_key = "sk-abcdef1234567890abcdef1234567890abcdef12"

# def main_chatBot(user_input):
#     response = openai.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": user_input},
#         ]
#     )
#     return response.choices[0].message.content  
# if __name__ == "__main__":
#     print("Virtual Assistant: Hi! I am your personal Virtual Assistant, How may I help you today?")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit", "bye"]:
#             print("Virtual Assistant: Goodbye!")
#             break
#         response = main_chatBot(user_input)
#         print(f"Virtual Assistant: {response}")


import random
import datetime


# Global joke state
joke_in_progress = False
joke_answer = ""

#JOKES
def get_jokes():
    jokes = [
        ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
        ("Why do Python programmers prefer using snakes?", "Because they can always find the right 'byte'!"),
        ("Why did the programmer quit his job?", "Because he didn't get arrays!"),
        ("Why do Java developers wear glasses?", "Because they don't see sharp!"),
        ("Why was the JavaScript developer sad?", "Because he didn't know how to 'null' his feelings!"),
        ("Why do programmers hate nature?", "It has too many bugs!"),
        ("Why don’t Python devs fight?", "They just resolve their conflicts in a virtual environment.")
    ]
    return random.choice(jokes)

#FACTS
def get_facts():
    facts = [
        "Python is widely considered one of the easiest programming languages to learn.",
        "The name 'Python' comes from the comedy series 'Monty Python’s Flying Circus'.",
        "Python supports object-oriented, procedural, and functional programming styles.",
        "Python has a huge standard library for common tasks like file handling and web development.",
        "Python is dynamically typed—no need to declare variable types!",
        "Python is open-source and has a huge community.",
        "Python is used in AI, machine learning, web development, data science, and more."
    ]
    return random.choice(facts)

#HELP
def help_topics():
    return (
        "Sure! What do you need help with?\n"
        "Help topics include:\n"
        "1. Learn Python\n"
        "2. Current time and date\n"
        "3. Simple games\n"
        "4. Random facts\n"
        "5. Jokes"
    )

#TIME / DATE
def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def get_current_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

#ACTIVITY WRAPPER
def wrap_up_activity(result):
    return f"{result}\n\nProgram complete. Returning to help section...\n\n{help_topics()}"

# SIMPLE GAMES

# Math Game
def math_game():
    operations = ['+', '-', '*', '/']
    user_choice = random.choice(operations)

    if user_choice == '+':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 + num2

    elif user_choice == '-':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, num1)
        answer = num1 - num2

    elif user_choice == '*':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        answer = num1 * num2

    elif user_choice == '/':
        num2 = random.randint(1, 100)
        answer = random.randint(1, 100)
        num1 = answer * num2
        answer = num1 / num2

    else:
        return "Invalid operation selected. Please try again."

    print(f"Let's get started!: What is {num1} {user_choice} {num2}?")
    
    user_answer = input("Your answer: ")
    user_answer = float(user_answer)
    
    if round(user_answer, 2) == round(answer, 2):
        return "Correct! Well done!"
    else:
        return f"Incorrect. The correct answer is {answer}."
    
    

# Rock Paper Scissors
def rock_paper_scissors():
    print("You selected Rock, Paper, Scissors!")
    print("Let's play a game of Rock, Paper, Scissors!")
    print("You can type 'exit' or 'quit' to stop playing at any time.")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice in ["exit", "quit"]:
            return "Thanks for playing! Goodbye!"

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "You win!"
        else:
            return "You lose! Better luck next time!"

# Guess the Number
def guess_game():
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 10. Can you guess it?")
    number = random.randint(1, 10)
    
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess == number:
        return "Congratulations! You guessed the right number!"
    else:
        return f"Sorry, the correct number was {number}."

#PYTHON RESOURCES
def python_resources():
    return (
        "Here are some great resources to learn Python:\n"
        "1. Codecademy – Interactive Python course\n"
        "2. Coursera – Python for Everybody\n"
        "3. Automate the Boring Stuff with Python – Free book\n"
        "4. Python.org – Official documentation\n"
        "5. W3Schools – Python tutorial\n"
        "6. Real Python – In-depth tutorials\n"
        "7. LeetCode / HackerRank – Practice problems\n"
        "8. YouTube – Corey Schafer, freeCodeCamp, Tech With Tim\n"
        "9. Python Crash Course – Excellent beginner book"
    )

#MAIN CHATBOT FUNCTION
def main_chatBot(user_input, user_name=""):
    global joke_in_progress, joke_answer
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ["hello", "hi"]):
        return f"Hello {user_name}! How can I assist you today?"

    elif any(name_query in user_input for name_query in ["what is your name", "who are you"]):
        return "I am your virtual assistant. You can call me Chipee."

    elif "help" in user_input:
        return help_topics()

    # Joke Setup
    elif "tell me a joke" in user_input:
        question, answer = get_jokes()
        joke_in_progress = True
        joke_answer = answer
        return question

    # Joke Punchline
    elif joke_in_progress and "why" in user_input:
        joke_in_progress = False
        return wrap_up_activity(joke_answer)

    elif joke_in_progress:
        return "Just say 'why?'"

    elif "tell me a fact" in user_input or "random facts" in user_input:
        return wrap_up_activity(get_facts())

    elif "game" in user_input:
        return (
            "Sure! Which game would you like to play?\n"
            "1. Math Game\n"
            "2. Guess the Number Game\n"
            "3. Rock Paper Scissors\n"
            "Type 'math' for Math Game, 'guess' for Guess the Number Game, or 'rock' for Rock Paper Scissors."
        )

    elif "math" in user_input:
        return wrap_up_activity(math_game())

    elif "guess" in user_input:
        return wrap_up_activity(guess_game())

    elif "rock" in user_input:
        return wrap_up_activity(rock_paper_scissors())

    elif "learn python" in user_input:
        return (
            "Python is a versatile programming language! Would you like some learning resources?\n"
            "If yes, just type 'yes'."
        )

    elif user_input.strip() in ["yes", "sure", "yeah"]:
        return wrap_up_activity(python_resources())

    elif user_input.strip() in ["no", "nope", "not now"]:
        return "No problem! If you change your mind, just ask for Python resources."

    elif "time" in user_input:
        return f"The current time is {get_current_time()}."

    elif "date" in user_input:
        return f"Today's date is {get_current_date()}."

    else:
        return "I'm not sure how to respond to that. Try typing 'help' to see what I can do."

#MAIN PROGRAM LOOP
if __name__ == "__main__":
    print("Virtual Assistant: Hello! I'm Chipee, your personal Virtual Assistant.")
    user_name = input("Virtual Assistant: What is your name? ")
    print(f"Virtual Assistant: Nice to meet you, {user_name}!")
    print("Virtual Assistant: How may I assist you today? Type 'help' for options.")

    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print(f"Virtual Assistant: Goodbye, {user_name}!")
            break
        response = main_chatBot(user_input, user_name=user_name)
        print(f"Virtual Assistant: {response}")