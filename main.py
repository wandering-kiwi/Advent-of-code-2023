lst = list(filter(lambda x: x, [index+1 if not list(filter(lambda x: x, [i if (int(i[0]) > 12 and i[1]=='red') or (int(i[0]) > 13 and i[1]=='green') or (int(i[0]) > 14 and i[1]=='blue') else None for i in [k for sub in [[j[1:].split(' ') for j in i.split(',')] for i in txt.split(':')[1].split(';')] for k in sub]])) else None for index, txt in enumerate(open('day2.txt', 'r'))]))

print(lst)


for index, txt in enumerate(open('day2.txt', 'r')):
  print(index+1)
  if not list(filter(lambda x: x, [i if (int(i[0]) > 12 and i[1]=='red') or (int(i[0]) > 13 and i[1]=='green') or (int(i[0]) > 14 and i[1]=='blue') else None for i in [k for sub in [[j[1:].split(' ') for j in i.split(',')] for i in txt.split(':')[1].split(', ')] for k in sub]]))

