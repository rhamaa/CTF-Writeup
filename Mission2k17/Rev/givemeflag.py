from z3 import *

v = [BitVec("num{0}".format(i),32) for i in range(20)]

s = Solver()
for i in range(len(v)):
	s.add(Or(And(v[i] > 47, v[i] <= 57), And(v[i] > 96, v[i] <= 122),And(v[i] > 64, v[i] <= 90), Or(v[i] == 33, v[i] == 63)))

s.add(v[11] * v[2] + v[18] + 8 == 25 * v[16])
s.add(v[5] + (v[1] - 2) / 2 == v[8])
s.add(122 * (v[12] - v[8]) == v[1])
s.add(v[4] - v[16] == v[2] - 1)
s.add(v[6] - v[19] == v[7])
s.add(v[5] + v[18] - v[13] + 3 == v[11])
s.add(v[1] + v[4] - (v[7] + v[10]) == v[9] + 4)
s.add(v[5] + v[3] + v[1] + v[7] + 10899 == 137 * v[14])
s.add(v[15] * v[17] == v[15] * v[10] + 1512)
s.add(v[15] + v[17] == v[1] + v[10])
s.add((v[3] - v[12]) * v[11] == v[19] + 3)
s.add((v[10] * v[2] - v[1]) / 2 == 22 * v[13] - 32)


# s.add(And(v[11] * v[2] + v[18] + 8 == 25 * v[16],v[5] + (v[1] - 2) / 2 == v[8],122 * (v[12] - v[8]) == v[1],v[4] - v[16] == v[2] - 1,v[6] - v[19] == v[7],v[5] + v[18] - v[13] + 3 == v[11],v[1] + v[4] - (v[7] + v[10]) == v[9] + 4,v[5] + v[3] + v[1] + v[7] + 10899 == 137 * v[14],v[15] * v[17] == v[15] * v[10] + 1512,v[15] + v[17] == v[1] + v[10],(v[3] - v[12]) * v[11] == v[19] + 3,(v[10] * v[2] - v[1]) / 2 == 22 * v[13] - 32))

print s.check()
m = s.model()
print m
print "".join([chr(m[i].as_long()) for i in v])
# hasil = [str(m[i].as_long()) for i in v]
# print "".join(map(chr,map(int,hasil)))
