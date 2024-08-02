import math
import random

def generate_prime_num(min_value, max_value):
    prime = random.randint(min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def mod_inverse(e, phi):
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