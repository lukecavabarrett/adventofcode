from dataclasses import dataclass
from functools import cached_property

@dataclass(repr=False)
class Dir(dict):
  @cached_property
  def size(self):
    return sum((x.size if isinstance(x,Dir) else x) for x in self.values())
  def walk_dirs(self):
    yield self
    for x in self.values():
      if isinstance(x,Dir):
        yield from x.walk_dirs()

class State:
  root : Dir
  def __init__(self):
    self.root = Dir()
    self.cwd = None
    self.lsd = set()
  def cd(self,d):
    if d=='/':
      self.cwd = [self.root]
    elif d=='..':
      self.cwd.pop()
    else:
      cwd = self.cwd[-1]
      assert d in cwd, cwd
      cwd = cwd[d]
      self.cwd.append(cwd)
  
  def ls(self,lines):
    cwd = self.cwd[-1]
    self.lsd.add(id(cwd))
    for line in lines:
      t,n = line.strip().split()
      if t=='dir':
        cwd[n] = Dir()
      else:
        cwd[n] = int(t)
  
  def check_dir(self):
    return self._check_dir(self.root,path='/')

  def _check_dir(self, root, path):
    if id(root) not in self.lsd:
      raise RuntimeError(f"directory {path} was not explored")
    for k,v in root.items():
      if isinstance(v,int): continue
      self._check_dir(v,path+k+'/')
    
  


def parse(fp):
  ls_call = None

  state = State()

  def submit_ls_call():
    nonlocal ls_call
    if ls_call is None: return
    state.ls(ls_call)
    ls_call = None

  for line in fp:
    line = line.strip()
    if line.startswith('$'):
      submit_ls_call()
      _,cmd,*args = line.split()
      if cmd=='ls':
        ls_call=[]
      else:
        assert cmd=='cd'
        assert len(args)==1
        state.cd(args[0])
    else:
      ls_call.append(line)
  submit_ls_call()

  state.check_dir()
  return state

fp = open('input.txt')
state = parse(fp)

def solve_1(state:State):
  return sum(d.size for d in state.root.walk_dirs() if d.size<=100000)

def solve_2(state:State):
  to_free = state.root.size - 40000000
  return min(d.size for d in state.root.walk_dirs() if d.size>=to_free)

print(solve_1,solve_1(state))
print(solve_2,solve_2(state))
