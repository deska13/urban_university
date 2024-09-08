def check_prime(number) -> bool:
    if number <= 1:
        return False
    else:
        for x in range(2, int(number**0.5) + 1):
            if number % x == 0:
                return False
    return True


def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if check_prime(res):
            print("Простое")
        else:
            print("Составное")
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
