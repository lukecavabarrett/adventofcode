import re

fp = iter('''    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2'''.split('\n'))

fp = open('input.txt')

def parse(fp):
    stks : list[list[str]] = []
    for line in fp:
        line = line.rstrip()
        if not line: break
        # print(list(enumerate(line[i].strip() for i in range(1,len(line),4))))
        for i,v in enumerate(line[i].strip() for i in range(1,len(line),4)):
            if not v: continue
            while i>=len(stks): stks.append([])
            stks[i].append(v)
    for l in stks:
        l.pop()
        l.reverse()

    p = re.compile(r'move\ (\d*)\ from\ (\d*)\ to\ (\d*)')
    moves = []
    for line in fp:
        moves.append(tuple(map(int,p.fullmatch(line.strip()).groups())))

    return stks, moves

stks, moves = parse(fp)

def solve_1(stks,moves):
    stks = list(map(list,stks))
    for qty,f,t in moves:
        f-=1
        t-=1
        for _ in range(qty): stks[t].append(stks[f].pop())
    return ''.join(s[-1] for s in stks)

def solve_2(stks,moves):
    stks = list(map(list,stks))
    for qty,f,t in moves:
        f-=1
        t-=1
        m = stks[f][-qty:]
        for _ in range(qty): stks[f].pop()
        stks[t].extend(m)
    return ''.join(s[-1] for s in stks)

print(solve_1(stks,moves))
print(solve_2(stks,moves))