matches = [sum([k[1].count(l) for l in k[0]]) for k in [[list(filter(lambda x: x, j.split(' '))) for j in i.strip('\n').split(':')[1].split('|')] for i in open('day4.txt', 'r')]]
copies = [1 for i in matches]
for m in range(214):
  copies[m+1:m + matches[m]+1] = [x + copies[m] for x in copies[m+1:m + matches[m]+1]]
print(sum(copies))
