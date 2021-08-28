# A simple function that generates a password of fixed length determined by a desired length

import random
import string

def password_generator(length):
    
    pool_of_chars = string.printable

    random_generation = [random.choice(pool_of_chars) for i in range(length)]
    password = "".join(random_generation)
    print(password.strip())
    return password

password_generator(22)
