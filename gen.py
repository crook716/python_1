'''
this is a module for demonstration the use of if the use of generator execution

'''

def run_take():
    '''
    Test the take() function

    '''
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def distinct(ieterable):
    '''
    return unique items by eliminating duplicates

    :param ieterable: the source series
    :yield: unique elements in order form
    '''
    seen=set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)
def run_pipeline()
    items + [3, 5, 5, 2,1, 1]
    for item in take(3, distinct(items)):
        print(item)

def run_distinct():
    items = [5, 7, 7, 6, 6, 5]
             for item in distinct(items):
                 print(item)
    def main()
    run_take()

def take(count, iterable):
    '''
    take items from the front of an iterable

    :param count: the maximum number of items to retrieve
    :param iterable: the source series
    :yields: At most 'count' items for 'iterable'
    '''

    counter=0
    for item in iterable:
        if counter==count:
            return
        counter +=1
        yield item