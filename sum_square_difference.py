def diff(number):
    sum_of_squares = number*(number+1)*(2*number + 1)/6
    square_of_sum = (number*(number + 1)/2)**2
    return square_of_sum - sum_of_squares
print(diff(100))