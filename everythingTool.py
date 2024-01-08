# Import necessary libraries
from nltk.corpus import wordnet as wn

# Define functions
def get_definition(word):
    # Retrieve synsets (groups of synonymous words) for the given word
    synsets = wn.synsets(word)
    
    if synsets:
        # Consider the first synset (most common usage) for simplicity
        first_synset = synsets[0]
        return first_synset.definition()
    else:
        # Handle case when no synsets are found
        return "Definition not found"
    
# Handling Maths
# Addition
def add(val1, val2):
    return float(val1) + float(val2)

# Subtraction
def subtract(val1, val2):
    return float(val1) - float(val2)

# Multiplication
def multiply(val1, val2):
    return float(val1) * float(val2)

# Division
def divide(val1, val2):
    # Handling divided by 0
    if val1 == 0 or val2 == 0:
        return "∞"
    else:
        return float(val1) / float(val2)
    
def calculator():
        symbol_name = ""
        
        operator = input("\nEnter an operator: ")

        if operator == "+":
            symbol_name = "add"

        elif operator == "-":
            symbol_name = "subtract"

        elif operator == "*" or operator == "x":
            symbol_name = "multiply"

        elif operator == "/" or operator == "%":
            symbol_name = "divide"

        value_a = input(f"Enter a value to {symbol_name}: ")
        value_b = input(f"Enter a second value to {symbol_name}: ")

        if operator == "+":
            print(add(value_a, value_b))

        elif operator == "-":
            print(subtract(value_a, value_b))

        elif operator == "*" or operator == "x":
            print(multiply(value_a, value_b))

        elif operator == "/" or operator == "%":
            print(divide(value_a, value_b))
        
        else:
            print("An Error Occurred. Please Try Again.")


# Seperate functions for Dictionary
def dictionary():
    word = input("Enter a word: ")
    print(get_definition(word))

# Main program
print("\n\nWelcome to Everything Tool™! Please select one of the following options:")

def Main():
    print("""
Enter the number of the option you want:
1. Calculator
2. Dictionary
4. Exit      
    """)

    opt = input()

    if opt == "1":
        calculator()
        Main()
    elif opt == "2":
        dictionary()
        Main()
    elif opt == "4":
        pass
    else:
        print("Invalid option. Please try again.")
        Main()

Main()