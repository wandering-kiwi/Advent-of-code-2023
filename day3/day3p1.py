lst = [''.join(map(lambda x: x if x in '0987654321.' else '*', i.strip('\n'))) for i in open('day3.txt', 'r')]

