# s = {1, 2, 3}
# e = set()
# print(s, type(s))

s1 = { 1, 2, 3, 4}
s2 = { 4, 1, 3, 7}
print(s1.intersection(s2))
print(s1.union(s2))
print({1,2}.issubset(s1))
print(s1.issupperset({1,2}))

