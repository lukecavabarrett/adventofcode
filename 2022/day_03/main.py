from collections import Counter
import itertools

input = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''.split('\n')

def cost(char:str):
    if char.isupper():
        return 26+cost(char.lower())
    return ord(char)-ord('a')+1

def solve_1(input:list[str])->int:
    return sum(
        cost(char)
        # (char,cnt)
        for line in input
        for char,cnt in (Counter(line[:len(line)//2]) & Counter(line[len(line)//2:])).items())


def take(iterable, n):
    iterable = iter(iterable)
    while True:
        x = list(itertools.islice(iterable, n))
        if not x: return
        yield x

def solve_2(input:list[str])->int:
    return sum(cost(char) for a,b,c in take(input,3) for char in (Counter(a)&Counter(b)&Counter(c)))

solve_2(input)