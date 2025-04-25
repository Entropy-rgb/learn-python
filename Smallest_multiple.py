smallest_number = 0
number_to_check = 1
#abhi smallest number ko 1 bol diya aise hi
while smallest_number == 0:
    no_of_divisors = 0
    for i in range(1,21):
        if number_to_check%i == 0:
            no_of_divisors = no_of_divisors + 1
        else:
            pass
    if no_of_divisors == 20:
        smallest_number = number_to_check
    else:
        number_to_check = number_to_check + 1
print(smallest_number)
