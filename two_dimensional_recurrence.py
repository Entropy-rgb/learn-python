#memoization of fibonnacci(n) is remaining and also this problem is under solving


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibonacci_memo[n-1] = fibonacci[n-1]
        fibonacci_memo[n-2] = fibonacci[n-2]        
        return fibonacci(n-1) + fibonacci(n-2)

fibbonaci_dictionary = {

}

for i in range(0,51):
    fibbonaci_dictionary[i] = fibonacci(i)
