#Funciones auxiliares
import constants as c

def is_prime(num):
    if num > 1:
        for i in range( 2, int(num/2 + 1)):
            if(num % i == 0):
                return False
        return True
    else:
        return True

def calculate_primes(start, finish):
    primes = []
    for n in range(start, finish):
        if is_prime(n) and n not in c.SKIP_RANGE:
            primes.append(n)
    return primes
    