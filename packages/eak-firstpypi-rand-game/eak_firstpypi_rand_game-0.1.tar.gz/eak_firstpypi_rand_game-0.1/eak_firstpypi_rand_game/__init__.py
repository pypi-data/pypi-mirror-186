from random_number_generator import generate_number, get_guess, calculate_delta

rand = generate_number()
inp = get_guess()
calculate_delta(rand, int(inp))