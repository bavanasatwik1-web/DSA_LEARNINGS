# 6. Find the union of two sets.
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))

# 7. Find the intersection of two sets.
# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))

# 8. Find the elements present in a but not in b.
# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# print(a.difference(b))

n=[2,2,2,4,3,4,5,5,6,7]
d={}
for j in n:
    d[j]=d.get(j,0)+1
for i in n:
    print(i,"-->",d[i])
                        