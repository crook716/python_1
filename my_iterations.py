'''
When working with iterators, henerators, etc.
look at the documentation for the itertools module
'''

from itertools import islice, count
from list_comprehension import is_prime

def main():

    thousand primes=islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type_(thousand primes))
    print("list of first 1K prime numbers:", list(thousand_primes))
    print("sum of first 1K prime numbers:", sum(list(thousand_primes)))
    # Note: if you need to use the object again, you need to re-generate it
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type_(thousand_primes))
    # Other built-ins use with itertools: any ("or"), or all ("and")
    print(any([False, False, True]))
    print(all([False, False, True]))
    print("are there prime numbers between 1328 1361",
          any(is_prime(x) for x in range(1328, 1362)))

