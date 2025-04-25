import math

def is_prime(number):
    """
    Checks if a number is prime efficiently.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def largest_prime_factor(number):
    """
    Finds the largest prime factor of a number efficiently.
    """
    largest_factor = 1

    # Handle factor 2 separately
    while number % 2 == 0:
        largest_factor = 2
        number //= 2

    # Handle odd factors
    # We only need to check up to the square root of the remaining number
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            largest_factor = i
            number //= i

    # If the remaining number is a prime factor greater than 2
    if number > 2:
        largest_factor = number

    return largest_factor

# The number for which we want to find the largest prime factor
number_to_factorize = 600851475143

# Find the largest prime factor
largest_factor_of_given_value = largest_prime_factor(number_to_factorize)

# Print the result
print(largest_factor_of_given_value)