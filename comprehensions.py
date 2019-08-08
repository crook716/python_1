'''

'''
from math import factorial
from pprint import pprint as pp
words="today i am very happy to learn about list comprehensions".split()
print(words)
data={}  #empty list
info={}  #empty list
def is_prime(num):

for word in words:
    #some analysis
    data.append(word)

    #filter data
    print(data)

    #task find the length of the first 20 factorial numbers
    for x in ramge(200)
    print(factorial(x))
    info.append(len(str(factorial(x))))

    #use a comprehension {}instead
    info2=[len(stri(factorial(x)))] for x in range(200)
    print(info2, type(info2))
    #set comprehensions:()

    info3 = {len(stri(factorial(x)))} for x in range(200)
   pp(info3)


# dictionary comprehensions
nba_teams={'jazz':'slc', 'warriors':'oakland', 'lakers':'LA'}
teams_nba={city:mascot for mascot, city in nba_teams.items()}
pp(teams_nba)


# filter predicates
if num<2 return false
    for i in range(2, int(sqrt(num)))+1:
        if num %i==0:
            return False
    primes=[x for x in range(1001) if is_prime(x)]
    print(len(primes), primes)


