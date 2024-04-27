from dsa.common.util import is_greater, negate


f = is_greater
g = negate(f)
print(f(5, 4))
print(g(5, 4))

