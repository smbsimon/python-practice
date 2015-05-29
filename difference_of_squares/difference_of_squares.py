def square_of_sum(x):
    sum = 0
    for i in range(1, x + 1):
        sum += i
    return sum ** 2

def sum_of_squares(y):
    sum = 0
    for i in range(1, y + 1):
        i = i ** 2
        sum += i
    return sum

def difference(n):
    return square_of_sum(n) - sum_of_squares(n)
