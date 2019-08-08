'''
Learn bout iterable, iterator objects
use the built in:
 iter(): create an iterable object,
, next(): fetch th enext element in the iterable object

def first(iterable):
'''
iterator=iter(iterable)
try:
    return next(iterator)
except StopIteration:
    raise ValueEerror("iterable is empty")
iterable=['spring', 'summer', 'fall', 'winter']
iterator=iter(iterable)  #give me an iterator
print(type(iterator), iterator)
print(next(iterator))
