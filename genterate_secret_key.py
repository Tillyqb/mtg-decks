from random import choice


def generate_random_hex(chars):
    primes = []
    key = ''
    with open("primes.txt", "r") as f:
        for line in f:
            line_list = line.split()
            for item in line_list:
                primes = primes + [int(item)]
    for i in range(chars):
        char = str(hex(choice(primes) * choice(primes)))[-1]
        key = key + char
    return key
