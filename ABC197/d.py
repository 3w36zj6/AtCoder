import cmath
N = int(input())
x0, y0 = map(int, input().split())
xm, ym = map(int, input().split())

xc = (x0 + xm) / 2
yc = (y0 + ym) / 2

z0 = complex(x0, y0)
zc = complex(xc, yc)
rot = cmath.e ** (2 * cmath.pi / N * 1.0j)
z1 = zc + (z0 - zc) * rot
print(z1.real, z1.imag)
