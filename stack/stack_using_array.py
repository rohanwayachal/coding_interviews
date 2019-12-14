class Stack:
  def __init__(self,size):
    self.size=size
    self.arr=[]
    self.top=-1

  def push(self,elem):
    if self.size<=len(self.arr):
      print("sorry, stack is full")
      return False
    else:
      self.arr.append(elem)
      self.top+=1
    
  def pop(self):
    if self.top==-1:
      print("sorry, nothing to pop")
      return None
    else:
      self.top-=1
      return self.arr.pop()
    
  def peek(self):
    if self.top==-1:
      print("sorry nothing to peek")
      return None
    else:
      return self.arr[self.top]

if __name__=='__main__':
  
  mystack=Stack(10)
  mystack.pop()
  mystack.push(1)
  mystack.push(2)
  mystack.push(3)
  mystack.push(4)
  print(mystack.arr)
  print(mystack.peek())
  print(mystack.pop())
  print(mystack.arr)
