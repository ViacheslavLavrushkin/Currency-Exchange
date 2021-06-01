import random
import string


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)
    return password
