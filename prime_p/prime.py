from prime_p.aux_functions import *
import prime_p.constants as c

class Prime:
    
    def __init__(self, p_start, p_finish):
        self.start = p_start
        self.finish = p_finish
    
    def calculate_primes(self):
        primes = []
        for n in range(self.start, self.finish):
            if is_prime(n) and n not in c.SKIP_RANGE:
                primes.append(n)
        return primes

    def prettify(self):
        body = ''
        for result in self.calculate_primes():
            body += f'This is a prime number: {result} \n'
        return body
