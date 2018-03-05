from z3 import *

N = Ints("N1 N2 N3")
v5 = N[1] + N[2]
# solve((v5 + N[0]) == 1337)

# Distinct -> fungsi agar membedakan hasil setiap constraints
s = Solver()
s.add(Distinct(N[0], N[2], N[1]))
# s.add(Distinct(N[0], v5))
s.add(N[1] + N[2] + N[0] == 1337)
# s.add(v5 + N[0] == 1337)

s.check()
print s.model()
