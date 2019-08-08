'''
When working with iterators, henerators, etc.
look at the documentation for the itertools module
'''

from itertools import islice, count
from itertools import chain

from list_comprehension import is_prime


def main():

    thousand_primes=islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("list of first 1K prime numbers:", list(thousand_primes))
    print("sum of first 1K prime numbers:", sum(list(thousand_primes)))
    # Note: if you need to use the object again, you need to re-generate it
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    # Other built-ins use with itertools: any ("or"), or all ("and")
    print(any([False, False, True]))
    print(all([False, False, True]))
    print("are there prime numbers between 1328 1361",
          any(is_prime(x) for x in range(1328, 1362)),
          list(x for x in range(1328, 1362) if is_prime(x))
        # Check if all names in an iterable are in tiel form: First Letter capiatlize
    names = ["London", "New york", "Ogden"]
    print(all(name == name.title()for name in names))
    # Another built-in: zip()
monday = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9]
tuesday = [13, 14, 15, 15, 1, 17, 16, 16, 12, 12]
wednesday = [2, 3, 4, 5, 6, 7, 6, 5, 4, 6]
# (:6.1f) --6 char width, 1 decimal precision, floating point
for temps in zip(monday, tuesday, wednesday):
    print("mine={:4.1f}, max={:4.1f}, avg={:4.1f}".format(
        min(temps), max(temps), sum(temps)/len(temps)))
    # chain
all_temps = chain(monday, tuesday, wednesday)
    print("all temperatures>0", all(t>0 for t in all_temps))
