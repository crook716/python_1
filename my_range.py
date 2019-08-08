'''
learn about range() collection
'''


    def main():

    #default
    for i in range(5):
    print("now setting initial  value")
        print (i)
    #set the initial value: =5 to <10

    for i in range(5,10):
        print(i)

    #create a list from range
    l=list(range(5, 10))
    print(l, type(l))
    12=;ost(range(5,10))+list(range(30,40))
    print(12, type(12))
    #step argument (begin, stop, step)
    12=list range(0, 20, 2)
    print(13, type(13))
    #
    s=[0, 2, 3, 4, 6]
    for i in range(len(s)):
        print(s[i])
    #better way
    for v in s:
        print (v)

    #enumerate(): returns an iterable series
    t=[6, 789, 123, 98, 2, 22]
    for p in enumerate (t):
        print(p)
    #A better way
    for i, v in enumerate(t):
        print("i={}, ve{}".format(i, v))


