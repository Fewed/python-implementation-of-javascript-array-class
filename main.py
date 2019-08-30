from arr import *

arr = Array(1, 2, 7, 3, 5)
a = arr
b = arr.reverse().map(lambda x: x ** 2)
c = b.join('-')

print(a)
print(a.value)
print(b.value)
print(c)
