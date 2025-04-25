def palindrome(number):
    first_digit = int(number/100000)
    second_digit = int(number/10000) - 10*first_digit
    third_digit = int(number/1000) - 10*second_digit - 100*first_digit
    rev_str = 100*third_digit + 10*second_digit + first_digit
    last_three = number % 1000
    if rev_str == last_three:
        return True
    else:
        return False
largest_num = 0
for i in range(100000,999999):
    if palindrome(i)==True:
        for k in range(100,999):
            if i%k == 0:
                if len(str(int(i/k)))==3:
                    largest_num = i
                else:
                    pass
            else:
                pass
    else:
        pass
print(largest_num)