print(sum([int(''.join([list(filter(lambda x: x in '0123456789', i))[n] for n in (0, -1)]))for i in open('day1.txt', 'r')]))
