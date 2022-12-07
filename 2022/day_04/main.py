input = '''
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''.split()

input = open('input.txt')

def range_intersect(r1, r2):
    return range(max(r1.start,r2.start), min(r1.stop,r2.stop))

data = [[range(int(r.split('-')[0]),int(r.split('-')[1])+1) for r in line.strip().split(',')] for line in input]

def solve_1(data):
    return sum(range_intersect(a,b) in (a,b) for a,b in data)

def solve_2(data):
    return sum(bool(range_intersect(a,b)) for a,b in data)

print('solve_1',solve_1(data))
print('solve_2',solve_2(data))