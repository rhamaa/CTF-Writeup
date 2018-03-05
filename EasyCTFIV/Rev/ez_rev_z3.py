from z3 import *

f = [BitVec("f{}".format(i),32) for i in range(5)]

s = Solver()

for i in range(len(f)):
    s.add(f[i] <= ord("z"), f[i] >= ord(" "))

v4 = f[0] + 1
v5 = f[1] + 2
v6 = f[2] + 3
v7 = f[3] + 4
v8 = f[4] + 5

s.add(v4 == (v8 - 10))
s.add(v5 == 53)
s.add(v6 == 125)
s.add(v7 == 111)
s.add(v8 == (v7 + 3))

s.check()
m = s.model()
print "".join([ chr(m[i].as_long()) for i in f ])
