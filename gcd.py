
def Sort_Tuple(tup):
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst - i - 1):
            if (tup[j][1] > tup[j + 1][1]):
                tup[j],tup[j+1]=tup[j+1],tup[j]
    return tup


# Driver Code
tup = [('for', 24), ('is', 50), ('Geeks', 28),
       ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]

print(Sort_Tuple(tup))

