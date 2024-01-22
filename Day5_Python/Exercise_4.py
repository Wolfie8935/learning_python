# Write a function called count_primes() that requires a single
# numeric argument.
# This function must display on the screen how many prime
# numbers there are in the range from zero to that number
# included, and then return the number of prime numbers found.
# Note: By convention 0 and 1 are not considered prim

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes(n):
    prime_count = 0
    for i in range(n + 1):
        if is_prime(i):
            prime_count += 1
    print(f"There are {prime_count} prime numbers in the range from 0 to {n}.")
    return prime_count

result = count_primes(10)
print(f"Number of prime numbers: {result}")
