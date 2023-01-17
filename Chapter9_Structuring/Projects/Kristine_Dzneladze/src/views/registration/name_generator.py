import random
import string

letters = string.ascii_lowercase + string.ascii_uppercase + string.digits

def random_name():
    return  ''.join(random.choice(letters) for i in range(10))

