print(sum([int(2**(sum([i[1].count(j) for j in i[0]])-1)) for i in [[list(filter(lambda x: x, j.split(' '))) for j in i.strip('\n').split(':')[1].split('|')] for i in open('day4.txt', 'r')]]))