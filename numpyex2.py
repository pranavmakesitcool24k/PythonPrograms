# use numpy methods in python @pranav version 3.9
from numpy import *
# (array values, int/float etc.)
x = array([1, 2, 3, 4, 5], float)
print(x)

# (start, end, steps)
a = arange(0, 10, 2)
print(a)

# (start, end, no. of parts)
b = linspace(1, 7, 4)
print(b)

# (start, end, no. of parts)
c = logspace(1, 2, 2)
print(c)

# (number of zero's)
d = zeros(5)
print(d)

# (number of one's)
e = ones(5)
print(e)
