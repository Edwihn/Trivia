import random

def get_random_number(count ,min_value, max_value):
    #First, I created the list
    random_numbers = list()
    #The loop will repeat until the length of the list raises the count.
    while len(random_numbers) < count:
        #Generates a random number
        number = random.randint(min_value, max_value)
        #It adds the number to the list if the number is not in the list
        if number not in random_numbers:
            random_numbers.append(number)
    return random_numbers