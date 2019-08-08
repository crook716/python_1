"""
Learn about generator functions
-descrie iterable series with code functions
-Are lazy evaluated; the next value in the sequence is computed on demand
-can model infinite series/sequences: data streams, mathematical series with no end
-Can use pipelines

use the yeld keyword
"""


def gen123():
    yield 1
    yield 2
    yield 3

def gen246():
    print("about to yield 2")
    yield2
    print("about to yield 4")
    yield4
    print("about to yield 6")
    yield6

def main():
    '''
    test funtion
    :return: 
    '''

    g=gen123()
    print(g, type(g))
    # yield next value
    print(next(g))
    print(next(g))
# iterate over the generator function
    for v in gen123():
        print(v)

    h=gen246()
    print(next(h))
    print(next(h))
    print(next(h))
    print(next(h))
    