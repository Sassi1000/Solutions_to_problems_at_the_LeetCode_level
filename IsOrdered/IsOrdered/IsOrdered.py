import random

def is_ordered(x):
    c=0  
    for i in range(len (x)):
      if(x[i]%2==0):
          c+=1
      if(len(x)==c):    
          return True  
    for k in range(c,len (x)):       
      if(x[k]%2==1):
          c+=1
      if(len(x)==c):    
          return True
    return False
#### MAIN ####
y=[2,4,6,8,1,3,5,7]
print(is_ordered(y))        

def build_ordered(size, x, y):
    a=[0]*size
    left=0
    right=size-1
    while(left<=right):
        num=random.randint(x,y)
        if(num%2==0):
            a[left]=num
            left+=1
        else:
            a[right]=num
            right-=1
    return a
####  MAIN  ####
print(build_ordered(11, 33, 77))
print(build_ordered(6, 5, 144))



