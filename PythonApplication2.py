# import random

# def SimpleSearch(b,x):
#    for i in range(len(b)):
#       if(b[i]==x):
#          return i
#    return -1

# a=[0]*10
# a[0]=random.randint(1, 10)
# for i in range(1, len(a)):
#    a[i]=a[i-1]+random.randint(1, 5)
# for i in range(10):
#    print(a[i], end=" ")
# print()   
# print()   
# print(SimpleSearch(a,22))




import random

def BainarySearch(b,x):
   r=len(b)-1
   l=0
   while(l<r):
       m=(r+l)//2
       if(b[m]==x):
          return m
       if(x>b[m]):
          l=m+1
       else:
          r=m-1
   if(x==b[l]):
      return r
    return -1 
      
a=[0]*10
a[0]=random.randint(1, 10)
for i in range(1, len(a)):
   a[i]=a[i-1]+random.randint(1, 5)
for i in range(10):
   print(a[i], end=" ")
print()   
print()   
print(BainarySearch(a,22))
