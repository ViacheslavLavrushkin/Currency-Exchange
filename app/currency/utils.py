import random
import string
from decimal import Decimal


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)
    return password


def to_decimal(number: str) -> Decimal:
    """"

    """
    return Decimal(number).quantize(Decimal('0.01'))
