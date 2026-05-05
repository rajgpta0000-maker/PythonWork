import calc as c

c.sum(10, 20)
c.sub(10, 5)
c.square(5)

import test as t

t.sum(10, 20, 30)
t.sub(10, 5)

from test import *
from calc import sum, sub
# from test import *
sum(10, 20)
sub(10, 5)

