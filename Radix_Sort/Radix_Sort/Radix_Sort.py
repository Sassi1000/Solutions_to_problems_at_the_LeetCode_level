import random

class Queu:
    def __init__(self):
        self.__first=None
        self.__last=None
    def Insert(self, x):
        temp=Node(x, None)
        if(self.__first==None):
            self.__first=temp
        else:
            self.__last.SetNext(temp)
        self.__last=temp
    def Remove(self):
        x=self.__first.GetValue()
        temp=self.__first
        self.__first=self.__first.GetNext()
        temp.SetNext(None)
        return x
    def Head(self):
        return self.__first.GetValue()
    def IsEmpty(self):
        return self.__first==None
class Node:
    def __init__(self, value, next):
        self.__value=value
        self.__next=next
    def SetValue(self, value):
        self.__value=value
    def SetNext(self, next):
        self.__next=next
    def GetValue(self):
        return self.__value
    def GetNext(self):
        return self.__next
    
def Radix(a):
   z=1
   t=[None]*10
   for i in range(10):
       t[i]=Queu()
   for i in range(5):
       for k in range(len(a)):
           t[a[k]//z%10].Insert(a[k])
       p=0
       for b in range(10):
          while(not t[b].IsEmpty()):
               a[p]=t[b].Remove()
               p+=1
       z=z*10

def Stupid_Sorting(a):
   for i in range(len(a)):
       for j in range(i+1, len(a)):
           if(a[i]>a[j]):
               temp=a[i]
               a[i]=a[j]
               a[j]=temp
               
#### MAIN ####               
x=[0]*1000000
for i in range(1000000):
    x[i]=random.randint(10000,99999)
Radix(x)
print(x)
# Stupid_Sorting(x)
# print(x)

