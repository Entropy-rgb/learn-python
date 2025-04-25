from Largest_prime_factor import is_prime

summ = 0
for i in range(2,2000000):
    if is_prime(i)==True:
        summ = summ + i
    else:
        pass

print(summ)