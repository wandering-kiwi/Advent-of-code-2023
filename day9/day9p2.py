lst = [[int(j) for j in i.split()] for i in open('day9.txt', 'r')]

def factorial(n):
  return 1 if n==0 else n*factorial(n-1)
# goes from 0 - 20, so next value is 21

l=21
v = -51090942171709440000 # 21 factorial
# ans = 0
# for i in range(l):
#   x = factorial(i) * factorial(l-i-1) * (-1)**(l-i-1) * (l-i)
#   # print(int(v/x)*n[i])
#   ans+= int(v/x)*n[i]

# print(ans)

print(sum([sum([int(v/(factorial(i) * factorial(l-i-1) * (-1)**(l-i-1) * (-1-i)))*n[i] for i in range(l)]) for n in lst]))