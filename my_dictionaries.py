'''
learn about dictionaries

'''
from pprint import pprint as pp
    urls={"google": "www.google.com",
          "yahoo": "www.yahoo.com",
          "twitter":  "twitter.com",
          "wsu":    "weber.edu"}

    pp(urls, type(urls))
    #access by key: [key]
    pp(urls["wsu"])
    #build dictionary with dict() consturctor
    names_age=[('alice', 32), ('mario', 23), ('hugo', 21)
    d=dict(names_age)
    pp(d)
    #another method
    phonetic=dict(a='alpa', b='bravo', c='charlie', d='delta')
    pp(phonetic)
    #make a copy
    e=phonetic.copy()  #this will make a copy
    pp(e)
    #updating a dictionary: update() method
    stocks={'goog':891, 'aapl':416, 'IBM':194}
    pp(stocks)
    stocks.update({'goog':999, 'yhoo':2})
    pp(stocks)
    # Iteration default is by key
    for key in stocks:
        print("(k)=>{v}".format(k=key, v=stocks[key]))
        #iterate by values
        for val in stocks, values():
            pp("val=", val)
        #iterate by both key and value with items()
        for items in stocks.items():
            pp(items)
        for key, val in stocks.items():
            print(key, val)
        #test for membership via key
            print('goog'in stocks)
            print('windows' not in stocks)
        # deleting: del keyword
            print(stocks)
            del stocks['yhoo']
            print(stocks)
        # Mutability of Dictionaries
            isotopes= {
                'H':[1, 2, 3]
                'He':[3, 4]
                'Li':[6, 7]
                'Be':[7, 9, 10]
                'b':[10, 11]
                'C':[11, 12, 13, 14]
                print(isotopes)
                isotopes['H']+= [4, 5, 6, 7]
                print(isotopes)
                isotopes('N') = [13, 14, 15]


            }




