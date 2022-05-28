
ms1 = {3,4,5}
ms2 = {"hola", 23.3, False, True}
ms3 = {2,3,4,2,6,2,3,1}
empty_set = set()

print(ms1)
print(ms2)
print(ms3)
print(type(empty_set))

empty_set.add('1')
empty_set.add(int(33))
print(empty_set)

empty_set.update([1,5,8], (3,5))
print(empty_set)


empty_set.discard(1)
empty_set.discard(4)

print(empty_set)

empty_set.pop()
print(empty_set)

empty_set.clear()
print(empty_set)