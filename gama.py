import ast
import datetime
import operator
import random
import re

CREATOR = "prashanth"
CREATOR_CONTACT = "9398789171"  


# ---------- Greeting ----------
def get_greeting(hour, name):
    if hour < 12:
        return f"Happy morning! said by {CREATOR} to you, {name}"
    elif hour < 18:
        return f"Good afternoon! said by {CREATOR} to you, {name}"
    elif hour < 21:
        return f"Good evening! said by {CREATOR} to you, {name}"
    else:
        return f"Good night, {name}"


# ---------- Chatbot memory [ dictionary of responses ] ----------
responses = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm just a program, but I'm functioning as expected! How about you?",
    "what is your name": "I am GAMA, your friendly chatbot!",
    "cool": "I'm glad you think so! What else would you like to know?",
    "happy": "That's great to hear! What makes you happy?",
    "sad": "I'm sorry to hear that. Is there anything I can do to help?",
    "what are functions": "Functions are blocks of code that perform a specific task and can be reused throughout your program.",
    "what is a variable": "A variable is a storage location in programming that holds data which can be changed during program execution.",
    "what is a loop": "A loop is a programming construct that repeats a block of code as long as a specified condition is true.",
    "what is a list": "A list is a collection of items in programming that can be of different data types and can be modified.",
    "what is a dictionary": "A dictionary is a collection of key-value pairs in programming, where each key is unique and maps to a specific value.",
    "what is a class": "A class is a blueprint for creating objects in object-oriented programming, encapsulating data and behavior.",
    "what is an object": "An object is an instance of a class that contains data and methods defined by the class.",
    "what is inheritance": "Inheritance is a feature of object-oriented programming that allows a class to inherit properties and methods from another class.",
    "what is polymorphism": "Polymorphism is a concept in programming that allows objects of different classes to be treated as objects of a common superclass, enabling flexibility and code reuse.",
    "what is encapsulation": "Encapsulation is a principle of object-oriented programming that restricts access to certain components of an object, promoting modularity and protecting the internal state of the object.",
    "what is abstraction": "Abstraction is a programming concept that focuses on exposing only the essential features of an object or system while hiding the unnecessary details, allowing for simpler and more efficient code design.",
    "what is recursion": "Recursion is a programming technique where a function calls itself in order to solve a problem, often breaking it down into smaller subproblems until a base case is reached.",
    "what is a module": "A module is a file containing Python code that can define functions, classes, and variables, and can be imported and used in other Python programs.",
    "what is a package": "A package is a collection of Python modules organized in a directory hierarchy, allowing for better code organization and reuse.",
    "what is a decorator": "A decorator is a design pattern in Python that allows you to modify the behavior of a function or class method without changing its source code, often used for logging, access control, and other cross-cutting concerns.",
    "what is a generator": "A generator is a special type of iterator in Python that allows you to create an iterable sequence of values using a function with the 'yield' keyword, enabling efficient memory usage and lazy evaluation.",
    "what is a lambda function": "A lambda function is an anonymous, inline function in Python that can take any number of arguments but can only have a single expression, often used for short, throwaway functions.",
    "what is a list comprehension": "A list comprehension is a concise way to create lists in Python using a single line of code, often including a loop and an optional condition to filter elements.",
    "what is a set": "A set is an unordered collection of unique elements in Python that supports mathematical set operations like union, intersection, and difference.",
    "what is a tuple": "A tuple is an ordered, immutable collection of elements in Python that can contain mixed data types and is often used to group related data together.",
    "what is a string": "A string is a sequence of characters in programming that represents text and can be manipulated using various string methods and operations.",
    "what is a boolean": "A boolean is a data type in programming that can have one of two values: True or False, often used for conditional statements and logical operations.",
    "what is an integer": "An integer is a whole number in programming that can be positive, negative, or zero, and is used for counting, indexing, and arithmetic operations.",
    "what is a float": "A float is a data type in programming that represents a number with a decimal point, allowing for the representation of real numbers and fractional values.",
    "what is a complex number": "A complex number is a number in programming that consists of a real part and an imaginary part, often represented in the form a + bi, where 'a' is the real part and 'b' is the imaginary part.",
    "what is a data structure": "A data structure is a way of organizing and storing data in a computer so that it can be accessed and modified efficiently. Examples include arrays, linked lists, stacks, queues, trees, and graphs.",
    "what is an algorithm": "An algorithm is a step-by-step procedure or set of rules for solving a specific problem or performing a computation, often expressed in a programming language or pseudocode.",
    "what is a database": "A database is an organized collection of data that can be easily accessed, managed, and updated, often used to store information for applications and websites.",
    # --- small talk ---
    "good morning": "Good morning! I hope you have a wonderful day. What would you like to learn today?",
    "good afternoon": "Good afternoon! How is your day going?",
    "good evening": "Good evening! Ready to learn something new?",
    "good night": "Good night! Sleep well and see you tomorrow.",
    "thank you": "You're welcome! Ask me anything else you like.",
    "thanks": "You're welcome! Happy to help.",
    "who are you": f"I am GAMA, a chatbot created by {CREATOR}. I answer programming questions, do maths, and tell jokes.",
    "who made you": f"I was created by {CREATOR} using Python.",
    "who created you": f"I was created by {CREATOR}.",
    "how old are you": "I'm a new program, so I'm very young, but I learn more whenever my memory grows!",
    "i am bored": "Let's fix that! Try asking me for a joke, a maths calculation, or 'what is recursion'.",
    "i love you": "That's kind of you! I'm just a program, but I'm happy you like chatting with me.",
    # --- programming and tech ---
    "what is a function": "A function is a block of code that performs a specific task and can be reused throughout your program.",
    "what is python": "Python is a popular, easy-to-read programming language used for web development, data science, automation, AI, and more.",
    "what is html": "HTML (HyperText Markup Language) is the standard language used to structure the content of web pages.",
    "what is css": "CSS (Cascading Style Sheets) controls how web pages look: colors, fonts, spacing, and layout.",
    "what is javascript": "JavaScript is a programming language that makes web pages interactive.",
    "what is java": "Java is a widely used, object-oriented programming language known for running on many platforms, including Android apps and large systems.",
    "what is sql": "SQL (Structured Query Language) is used to store, search, and manage data in relational databases.",
    "what is an api": "An API (Application Programming Interface) is a set of rules that lets one program talk to another and share data.",
    "what is a bug": "A bug is a mistake or flaw in a program that makes it behave in an unexpected way.",
    "what is debugging": "Debugging is the process of finding and fixing bugs in your code, often by reading error messages and testing step by step.",
    "what is an error": "An error is a problem that stops a program from running properly. Read the message carefully because it usually tells you the line and the cause.",
    "what is git": "Git is a version control tool that tracks changes to your code so you can go back, compare, and work with others.",
    "what is github": "GitHub is a website where people store code using Git, share projects, and collaborate.",
    "what is a compiler": "A compiler translates source code into machine code that the computer can run directly.",
    "what is an interpreter": "An interpreter runs your code line by line instead of translating it all first. Python uses one.",
    "what is ai": "AI (artificial intelligence) is when computers do tasks that normally need human intelligence, like understanding language or recognizing images.",
    "what is machine learning": "Machine learning is a part of AI where computers learn patterns from data instead of being given exact rules.",
    "what is the internet": "The internet is a worldwide network of connected computers that share information, from websites to messages.",
    "what is a website": "A website is a collection of web pages, usually built with HTML, CSS, and JavaScript, that you open in a browser.",
    "what is an operating system": "An operating system, like Windows, Android, or Linux, manages a device's hardware and lets programs run.",
    "how to learn programming": "Start with one language such as Python, practice small projects every day, read other people's code, and don't be afraid of errors. Building things like this chatbot is a great way to learn.",
    "what is friendship": f"Friendship is a close and trusting relationship between two or more people, characterized by mutual support, understanding, and shared experiences. You can be friendly to {CREATOR}, he can understand you.",
    "fuck you":"fuck you toooooo"
}


SORTED_KEYS = sorted(responses, key=len, reverse=True)

EXIT_WORDS = ("bye", "exit", "quit")

FALLBACK = (
    f"I'm sorry, I don't know that yet. I was created by {CREATOR}, "
    f"ask him or message him. Contact: {CREATOR_CONTACT}"
)


# ---------- Helpers ----------
def is_exit(text):
    """True if the user typed a whole-word exit command."""
    words = re.findall(r"[a-z']+", text.lower())
    return any(word in EXIT_WORDS for word in words)


def get_response(user_question):
    """Return a reply, matching whole words/phrases only (so 'this' does not match 'hi')."""
    user_question = user_question.lower()
    for key in SORTED_KEYS:
        if re.search(rf"\b{re.escape(key)}\b", user_question):
            return responses[key]
    return FALLBACK


# ---------- Extra features ----------
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the Python programmer wear glasses? Because he couldn't C!",
    "There are 10 kinds of people: those who understand binary and those who don't.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why was the function sad? It didn't get any arguments.",
]

HELP_TEXT = (
    "Here is what I can do:\n"
    "  - Answer programming questions (e.g. 'what is a loop')\n"
    "  - Tell the time ('what time is it') or the date ('today's date')\n"
    "  - Tell a joke ('tell me a joke')\n"
    "  - Do maths ('calc 12 * (3 + 4)')\n"
    "  - Say 'bye' to exit"
)

_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _eval_node(node):
    """Safely evaluate a parsed maths expression (numbers and + - * / // % ** only)."""
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPERATORS:
        left, right = _eval_node(node.left), _eval_node(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("power too large")
        return _OPERATORS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPERATORS:
        return _OPERATORS[type(node.op)](_eval_node(node.operand))
    raise ValueError("unsupported expression")


def calculate(expression):
    try:
        result = _eval_node(ast.parse(expression, mode="eval").body)
        return f"The answer is {result:g}" if isinstance(result, float) else f"The answer is {result}"
    except ZeroDivisionError:
        return "I can't divide by zero!"
    except (ValueError, SyntaxError, OverflowError):
        return "Sorry, I couldn't calculate that. Try something like: calc 12 * (3 + 4)"


def get_special_response(text):
    """Handle commands that need code instead of a fixed answer. Returns None if no match."""
    text = text.lower().strip()

    match = re.match(r"^(?:calc|calculate)\s+(.+)$", text)
    if match:
        return calculate(match.group(1))

    if re.search(r"\bhelp\b|what can you do", text):
        return HELP_TEXT
    if re.search(r"what time|current time|time is it|time now", text):
        return "It is " + datetime.datetime.now().strftime("%I:%M %p")
    if re.search(r"\b(date|today)\b", text):
        return "Today is " + datetime.datetime.now().strftime("%A, %d %B %Y")
    if re.search(r"\bjoke\b|make me laugh", text):
        return random.choice(JOKES)
    return None


# ---------- Main ----------
def main():
    name = input("Enter your good name: ").strip() or "friend"

    print(get_greeting(datetime.datetime.now().hour, name))
    print(f"Hi! There, I am GAMA, nice to meet you, {name}!")
    print(f"You can ask any type of question to me and I will try to answer it for you, {name}.")
    print("Type 'help' to see everything I can do.")

    while True:
        user_input = input("You  : ").strip()
        if not user_input:
            continue

        if is_exit(user_input):
            print("GAMA : Goodbye! Have a great day! Focus on your work and keep learning new things. See you next time!")
            break

        reply = get_special_response(user_input) or get_response(user_input)
        print("GAMA : " + reply)


if __name__ == "__main__":
    main()