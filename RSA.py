import math
import random

def generate_prime_num(min_value, max_value):
    """
    Generate a random prime number within the given range.

    Parameters:
    min_value (int): The minimum value of the range.
    max_value (int): The maximum value of the range.

    Returns:
    int: A random prime number within the given range.
    """
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime

def is_prime(num):
    """
    Check if a given number is a prime number.

    Parameters:
    num (int): The number to be checked.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(e, phi):
    """
    Calculate the modular multiplicative inverse of e with respect to phi.

    This function iterates through possible values of d from 3 to phi (exclusive)
    and checks if (d * e) % phi equals 1. If such a d is found, it is returned.
    If no such d is found, a ValueError is raised indicating that the mod inverse does not exist.

    Parameters:
    e (int): The number for which the modular multiplicative inverse is to be calculated.
    phi (int): The modulus.

    Returns:
    int: The modular multiplicative inverse of e with respect to phi.

    Raises:
    ValueError: If the mod inverse does not exist.
    """
    for d in range(3, phi_n):
        if (d * e) % phi == 1:
            return d
    raise ValueError("Mod inverse does not exist.")

p, q = generate_prime_num(100, 500), generate_prime_num(100, 500)

while p == q:
    q = generate_prime_num(100, 500)

n = p * q
phi_n = (p - 1) * (q - 1)

e = random.randint(3, phi_n - 1)
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n - 1)

d = mod_inverse(e, phi_n)

your_message = input("Enter your message to encrypt: ")

print("Prime number P: ", p)
print("Prime number Q: ", q)
print("n: ", n)
print("Public key: ", e)
print("Private key: ", d)
print("Phi of n", phi_n)

message_encoded = [ord(ch) for ch in your_message]
print("Message in ASCII code", message_encoded)

ciphertext = [pow(ch, e, n) for ch in message_encoded]
print(your_message, " Ciphered in: ", ciphertext)

decode_message = [pow(ch, d, n) for ch in ciphertext]
print("Decrypt the ciphertext back to ASCII values", decode_message)

message = "".join(chr(ch) for ch in decode_message)
print("From ASCII to text: ", message)