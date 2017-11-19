from z3 import *

s = Solver()
v = [Int("v{}".format(i)) for i in range(30)]

for i in range(len(v)):
	s.add(v[i] >= 32,v[i] <=126)

s.add(v[1] + v[0] - v[2] == 81)
s.add( v[0] - v[1] + v[2] == 53)
s.add(v[1] - v[0] + v[2] == 87)
s.add(v[4] + v[3] - v[5] == 90)
s.add(v[3] - v[4] + v[5] == 156)
s.add( v[4] - v[3] + v[5] == 66)
s.add(v[7] + v[6] - v[8] == 98 )
s.add(v[6] - v[7] + v[8] == 140 )
s.add(v[7] - v[6] + v[8] == 92)
s.add(v[10] + v[9] - v[11] == 38 )
s.add(v[9] - v[10] + v[11] == 170)
s.add(v[10] - v[9] + v[11] == 60)
s.add(v[13] + v[12] - v[14] == 29)
s.add(v[12] - v[13] + v[14] == 161)
s.add(v[13] - v[12] + v[14] == 69)
s.add(v[16] + v[15] - v[17] == 163)
s.add(v[15] - v[16] + v[17] == 27 )
s.add(v[16] - v[15] + v[17] == 69)
s.add(v[19] + v[18] - v[20] == 147)
s.add(v[18] - v[19] + v[20] == 43)
s.add(v[19] - v[18] + v[20] == 59)
s.add(v[22] + v[21] - v[23] == 146)
s.add(v[21] - v[22] + v[23] == 86 )
s.add(v[22] - v[21] + v[23] == 44 )
s.add(v[25] + v[24] - v[26] == 67)
s.add(v[24] - v[25] + v[26] == 89)
s.add(v[25] - v[24] + v[26] == 75)
s.add(v[28] + v[27] - v[29] == 117)
s.add(v[27] - v[28] + v[29] == 125)
s.add(v[28] - v[27] + v[29] == 125)

s.check():
m = s.model()
print "Flag : %s" % ("".join(chr(m[v[i]].as_long()) for i in range(len(v))))
