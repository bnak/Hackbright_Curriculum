from arithmetic import *
from sys import exit

"""# No setup
repeat forever:
    read input
    tokenize input - function
        if the first token is 'q', quit - evaluation command function
    otherwise decide which math function to call based on the tokens we read - execution function

    """
def tokenize(user_input):
    tokens = user_input.split(" ")
    return tokens 

def convert_numbers(num):
    return float(num)

# """def check_num2(num):
#     if num[2]
#         return 
#     else 
# """

def execute_operator(operator, num1, num2):
    if operator == '+':
        return add(num1,num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1,num2)
    elif operator == 'square':
        return square(num1)
    elif operator == 'cube':
        return cube(num1)
    elif operator == 'pow':
        return power(num1, num2)
    elif operator == 'mod':
        return mod(num1,num2)
    else:
        print "Error"

def check_for_bad_input():
    #check for:
    #   presence of second and third argumetns
    #   whether second and third arguments are letters
    pass


def main():

    user_input = raw_input("> ")

    tokens_array = tokenize(user_input)

    while tokens_array[0] != 'q':        

        if len(tokens_array) < 2:
            num1 = 0
        else:
            num1 = convert_numbers(tokens_array[1])


        if len(tokens_array) < 3:
            num2 = 0
        else:
            num2 = convert_numbers(tokens_array[2])

        print execute_operator(tokens_array[0], num1, num2)

        user_input = raw_input("> ")
        tokens_array = tokenize(user_input)

    
if __name__== "__main__": 
    main()