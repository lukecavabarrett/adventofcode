

def read() -> list[tuple[int,int]]:
    _d_map = {
        'A':0,'B':1,'C':2,
        'X':0,'Y':1,'Z':2,
    }
    with open('input.txt') as fp:
        for line in fp:
            line = line.strip()
            if not line:
                return
            yield tuple(_d_map[c] for c in line.split())


def outcome(other:int,you:int)->int:
    if(other==you): return 3 # draw
    if((other+1)%3 == you): return 6 # you won
    return 0

def game_score(other:int,you:int)->int:
    return outcome(other,you)+you+1

def solve_1(input):
    return sum(game_score(o,y) for o,y in input)

def get_oc(other:int,outc:int)->int:
    if outc==0: return (other+2)%3 # need to lose
    if outc==1: return other # need to draw
    if outc==2: return (other+1)%3 # need to win

def uncurry(func):
    def f2(args):
        return func(*args)
    return f2

def solve_2(input):
    return solve_1((o,get_oc(o,oc)) for o,oc in input)

# input = [ (0,1) , (1,0) , (2,2) ]
# print(solve_1(input))
print(solve_1(read()))




