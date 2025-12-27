s = {1, 2, 3, 3, 5, 5, 6}
s1 = set([1, 2, 3, 3, 5, 5, 6])

print(s)
print(s1)

print("-----------------------------------------------------------------------------------------------------")

s.add(7)
print(s)

s.update([8, 9])
print(s)

s.remove(8)
print(s)

s.discard(10)
print(s)

print(s.union(s1))

print(s.intersection(s1))

print(s.symmetric_difference(s1))