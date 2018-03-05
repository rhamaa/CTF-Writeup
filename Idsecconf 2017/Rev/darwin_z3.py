from z3 import *

v18 = 13
v17 = 0
v16 = 0
v15 = 0
v14 = 0
v13 = 0
v12 = 0

s = Solver()
a1 = [BitVec("a{}".format(i),32) for i in range(v18)]

for i in range(v18):
    s.add(a1[i] <= ord("z"), a1[i] >= ord(" "))

for i in range(v18):

    if i % 2:
        v7 = a1[i] ^ v14
    else:
        v7 = v14
    v14 = v7
    if i % 2 == 1:
        v6 = v13;
    else:
        v6 = a1[i] ^ v13
    v13 = v6
    if i % 2:
        v5 = 0
    else:
        v5 = a1[i]
    v17 += v5
    if i % 2 == 1:
        v4 = a1[i] ^ v15
    else:
        v4 = v15
    v15 = v4

for j in range(v18/2):
    v12 ^= a1[j]

for k in range(v18):

    if k % 2:
        v3 = a1[k]
    else:
        v3 = 0
    v16 += v3
    if k % 2:
        v2 = v15
    else:
        v2 = a1[k] ^ v15;
    v15 = v2


    v4 = 13
    v3 = 23
    for i in range(v4):
        v3 = (a1[i] << i) + 7 * v3;
    v11 = v3 >> 4;

s.add(v17 % 10 == 8)
s.add(v11 == 0xFD4E6A44)
s.add(v12 == 21)
s.add(v14 == 56)
s.add(v15 == 90)
s.add(v16 % 10 == v17 % 10)
s.add((v16 + v17) / 10 == 116)
s.add((v16 + 2 * v17) / 10 == 183)
s.add(a1[1] == 51)
s.add(a1[5] == 53)
s.add(a1[8] == 52)
s.add(a1[10] == 55)

print s.check()

m = s.model()

print "".join([ chr(m[i].as_long()) for i in a1 ])
