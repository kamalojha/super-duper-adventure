import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a password with default length of 8 characters
password = generate_password()
print("Generated password:", password)

# Generate a password with a custom length of 12 characters
custom_length_password = generate_password(12)
print("Custom length password:", custom_length_password)
