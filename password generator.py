import random
import string

def generate_password(length):
# Generate a random string of lowercase letters, uppercase letters, and digits
password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=length))

# Add some special characters to the password
special_characters = '!@#$%^&*()-_=+'
password += ''.join(random.choices(special_characters, k=random.randint(1, length // 4)))

# Shuffle the characters in the password
password = list(password)
random.shuffle(password)
password = ''.join(password)

return password

# Test password generator
print(generate_password(12))
print(generate_password(16))
print(generate_password(24))