from z3 import *

s = Solver()
n = BitVec("X1",32)
f1 = 102
m = n ^ 0x58EB29
g = m * 1 ^ f1
s.add(g == 97)
print s.check()
m = s.model()
print "Valid PIN {}".format(m[n])