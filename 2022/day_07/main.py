class State:
  def __init__(self):
    self.root = {}
    self.cd = None
  def cd(self,d):
    if d=='/':
      self.cd = [self.root]
    elif d=='..':
      self.cd.pop()
    else:
      cd = self.cd[-1]
      assert d in cd
      cd = cd['d']
      self.cd.append(cd)
      
