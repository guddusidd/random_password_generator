import random
import string

def _rand_pass(length=100):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

password = _rand_pass()
print(password)

with open('_pass.txt', 'w') as file:
    file.write(password)
