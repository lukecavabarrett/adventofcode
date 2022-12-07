import itertools
from collections import deque
def solve(s:str, k=14)->int:
    s = iter(s)
    q = deque(itertools.islice(s, k))
    i = k
    while len(set(q))!=len(q):
        i+=1
        q.popleft()
        q.append(next(s))
    return i