import random

def generate_number():
    random_number = random.randint(0, 100)
    return random_number

def get_guess():
    ''' Function to get user input
        args:
        none
        
        Returns: 
        inp: int. The user input (guess)
    '''
    
    inp = input("Which number between 0 and 100 did you guess?")
    print(inp)
    return inp

def calculate_delta(rand, inp):
    delta = rand - inp
    print("The difference between your number {} and the random number {} is {}".format(inp, rand, delta))
    