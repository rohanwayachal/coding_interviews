class TreeNode:
  def __init__(self,val):
    self.val=val
    self.left=None
    self.right=None



def solution(root,f,s):
        # initial bfs queue
        q=[root]


        while q:
            qlen=len(q)
            temp=[]
            for _ in range(qlen):
                curr=q.pop(0)
                
                if not curr:
                    temp.append(None)
                    q.append(None)
                    q.append(None)
                    
                else:
                    temp.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    else:
                        q.append(None)
                    if curr.right:
                        q.append(curr.right)
                    else:
                        q.append(None)
            print(temp)
            
            check=all(v is None for v in temp)
              #no nodes found in tree
            if check:  
              return -1
            
            if f.val in temp and s.val in temp:
              return abs(temp.index(f.val)-temp.index(s.val))-1


if __name__=="__main__":
  root=TreeNode(3)
  root.left=TreeNode(9)
  root.right=TreeNode(20)
  root.left.left=TreeNode(5)
  root.right.right=TreeNode(6)



  ans=solution(root,root.left.left,root.right.right)
  print(ans)
