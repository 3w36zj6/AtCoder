from math import sin, cos, pi, sqrt

A, B, H, M = map(int,input().split())

t = M+60*H

pos_h = (A*cos(pi/2-2*pi*t/720), A*sin(pi/2-2*pi*t/720))
pos_m = (B*cos(pi/2-2*pi*t/60), B*sin(pi/2-2*pi*t/60))

#print(pos_h[0]-pos_m[0], pos_h[1]-pos_m[1])
print(sqrt((pos_h[0]-pos_m[0])**2+(pos_h[1]-pos_m[1])**2))