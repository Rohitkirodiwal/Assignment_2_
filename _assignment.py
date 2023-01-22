def em(n):
    return n[1]

list1 = [(4,1),(3,8),(4,0),(8,7)]
list1.sort(key=em)
print(list1)