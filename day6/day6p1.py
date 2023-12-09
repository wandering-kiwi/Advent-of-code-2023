from math import ceil
f=[i for i in open('day6.txt', 'r')]
lstSenior = f[0].split()[1:]
lstJunior = f[1].split()[1:]
ans = 1
for v, t in enumerate(lstSenior):
  ans *= ceil((int(t) + (int(t)**2 - 4*int(lstJunior[int(v)]))**0.5)/2-int((int(t) - (int(t)**2 - 4*int(lstJunior[int(v)]))**0.5)/2))-1


print(ans)