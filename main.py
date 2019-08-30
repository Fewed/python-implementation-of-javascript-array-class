from arr import *

arr = Array(1, 2, 7, 3, 5)
a = arr
b = arr.reverse().map(lambda x: x ** 2)
c = b.join('')
d = a.filter(lambda x: x % 2)
e = a.reduce(lambda acc, cur: acc + cur, 0)
f = a.slice(1, -2)
g = a.splice(1, 1, 42)

print(a)
print(a.value)
print(b.value)
print(c)
print(d.value)
print(e)
print(f.value)
print(g)
