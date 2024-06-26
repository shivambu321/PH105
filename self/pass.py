import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = 12  # You can adjust the length of the password
password = generate_password(length)
print("Generated Password:", password)
