lst = [''.join(map(lambda x: x if x in '0987654321.' else '*', i.strip('\n'))) for i in open('day3.txt', 'r')]

def left_or_right(line, n):
  if line[n] in '0987654321':
    return line[n]
  elif line[n+1] in '0987654321':
    return line[n+1]
  elif line[n-1] in '0987654321':
    return line[n-1]
  else:
    return - 1

for l, j in enumerate(lst):
  for m, k in enumerate(j):
    if k == '*':
      o = left_or_right(j, m)
      print(o)
      if o == -1:
        o = left_or_right(lst[l-1], m)
        print(o)
        if o == -1:
          o = left_or_right(lst[l+1], m)
          print(o)



