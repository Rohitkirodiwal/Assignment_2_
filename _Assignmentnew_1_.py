# Write a Python program to get a list, sorted in increasing order by the 
# last element in each tuple from a given list of non-empty tuples


# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def element(n):
    return n[1]
list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list1.sort(key=element)
print(list1)