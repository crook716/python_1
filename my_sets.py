'''
learn about sets
an unordered collection of unique, immutable objects
define it using { }
you can use the set() constructor to create one
'''
def main():


   # Pass
    p={6, 75, 21, 45}
    print(p, type(p))
    data=[1, 3, 5, 2, 88, 3, 1]
    print(data, type (data))
    # eliminate duplicates
    sdata=set(data)
    print(sdata, type(sdata))
    # iterate with format(
    for item in sdata:
        print(item)
        # supports membership testing; in, not in
    print(5 in sdata)
    # adding elements to sets:
    sdata.add(45)
    print(sdata)
    sdata.update([2, 99, 44, 33, 1, 2, 88])
    print(sdata)
    # removing elements
    sdata.remove(44)  # remove() method: raises Key error if not found
    print(sdata)
    sdata.remove(77)
    print(sdata)
    sdata.discard(77)  # discard does not raise error
    print(sdata)
    # copying sets
    bk_data=sdata.copy()
    print(bk_data is sdata)
    print(bk_data==sdata)
    #define some sets
    blue_eyes={"olivia", "Harry", "Lily", "Jack"}
    blond_hair={"Harry", "jack", "Amelia", "Mia", "Joshua"}
    smell_hcn={"Harry", "Amelia"}
    taste_ptc={"Harry", "Lily", "Amelia", "Lola"}
    o_blood={"Mia", "Joshua", "Lily", "Olivia"}
    b_blood={"Amelia", "Jack"}
    a_blood={"Harry"}
    ab_blood={"Joshua", "lola"}
    print(blue_eyes.union(blond_hair))
    print(blue_eyes.intersection(taste_ptc))
    print(smell_hcn.symmetric_difference(a_blood))
    print(blond_hair.difference(ab_blood))
    print(taste_ptc.issuperset(smell_hcn))



    # if__name__=='__main__':
        main()

