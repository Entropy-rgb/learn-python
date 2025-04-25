from Largest_prime_factor import is_prime


number_in_check = 2
starter = 0
while starter < 10001:
    if is_prime(number_in_check) == True:
        starter = starter + 1
    else:
        pass
    number_in_check = number_in_check + 1

print(number_in_check - 1)