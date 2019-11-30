def is_prime(num):
    if num < 2:
        return False
    x = 2
    while x**2 <= num:
        if num % x == 0:
            return False
        x += 1
    return True


assert is_prime(7) is True, "41 is prime"
assert is_prime(45) is False, "41 is prime"
assert is_prime(75) is False, "41 is prime"

assert is_prime(5099) is True, "5099 is prime"
assert is_prime(7) is  True, "7  is prime"
assert is_prime(41) is True, "41 is prime"
assert is_prime(5099) is True, "5099 is prime"