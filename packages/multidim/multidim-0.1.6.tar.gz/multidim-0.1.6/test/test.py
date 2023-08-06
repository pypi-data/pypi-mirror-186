import multidim

val = multidim.nball.volume(17)
print(val)
# 0.14098110691713894

val = multidim.nball.integrate_monomial((4, 10, 6, 0, 2), lmbda=-0.5)
print(val)
# 1.0339122278806983e-07

# or nsphere, enr, enr2, ncube, nsimplex

vol = multidim.nball.volume(17, symbolic=True)
print(vol)
# 512*pi**8/34459425