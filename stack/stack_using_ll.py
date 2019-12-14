class Node():
  def __init__(self,val):
    self.val=val
    self.next=None



class Stack:
  def __init__(self,size):
    self.size=size
    self.head=None
    self.top=-1

  def push(self,elem):
    if self.size-1<=self.top:
      print("sorry, stack is full")
      return False
    else:
      new=Node(elem)
      new.next=self.head
      self.head=new
      self.top+=1
    
  def pop(self):
    if self.top==-1:
      print("sorry, nothing to pop")
      return None
    else:
      self.top-=1
      node=self.head
      self.head=self.head.next
      return node.val
    
  def peek(self):
    if self.top==-1:
      print("sorry nothing to peek")
      return None
    else:
      return self.head.val

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
