class Stack:
  def __init__(self,size):
    self.size=size
    self.q1=[]
    self.q2=[]
    self.top=-1

  def push(self,elem):
    if self.size-1<=self.top:
      print("sorry, stack is full")
      return False
    else:
      if self.top==-1:
        self.q1.append(elem)
      else:
        while self.q1:
          self.q2.append(self.q1.pop(0))
        self.q1.append(elem)
        while self.q2:
          self.q1.append(self.q2.pop(0))
      self.top+=1

    
  def pop(self):
    if self.top==-1:
      print("sorry, nothing to pop")
      return None
    else:
      self.top-=1
      return self.q1.pop(0)
    
  def peek(self):
    if self.top==-1:
      print("sorry nothing to peek")
      return None
    else:
      return self.q1[0]

if __name__=='__main__':
  
  mystack=Stack(3)
  mystack.pop()
  mystack.push(1)
  print(mystack.peek())
  mystack.push(2)
  print(mystack.peek())
  mystack.push(3)
  print(mystack.peek())
  mystack.push(4)
  print(mystack.peek())
  print(mystack.pop())
