'''
generator objects asre a cross bewteen comprehension and generator functions
syntax; similar to list comprehension, but with parenthesis
    (expression of the item) for item in the iterable)
'''

def main():
    '''
    test function
    :return:
    '''

    m_sq=(x*x for x in range(1,1000001))
    print(m_sq, type(m_sq))
    print("the sum of the first 1 square million numbers is:", sum(m_sq))
    print("the sum of the first 1M square numbers is:",
          sum(x*x for x in range(1, 1000001)))
    #the sum of the prime numbers between 1 to 1M
    from list_comprehension import is_prime
    print("the sum of the first 1M prime numbers is:",
          sum(x * x for x in range(1, 1000001) if is_prime(x)))