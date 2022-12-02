
def read():
  y = []
  current = []
  with open('input.txt') as fp:
    for line in fp:
      line = line.strip()
      if not line:
        y.append(current)
        current = []
      else:
        current.append(int(line))
  return y
  
def solve_1(input : list[list[int]]) -> int:
  return max(map(sum,input))

def solve_2(input : list[list[int]], k=3) -> int:
  return sum(sorted(map(sum,input),reverse=True)[:k])
