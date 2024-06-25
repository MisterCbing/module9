def simple(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_prime(func):
    def wrapper(*args):
        temp = func(*args)
        print('Простое' if simple(temp) else 'Составное')
        return temp
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)
result = sum_three(4, 7, 1)
print(result)