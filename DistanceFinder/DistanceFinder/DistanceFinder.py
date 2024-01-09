def DistanceFinder(a, num):
    left=0
    while(left<len(a) and a[left]!=num):
        left+=1
    if(left==len(a)):
        return -1
    right=len(a)-1
    while(a[right]!=num):
        right-=1
    return left+(len(a)-1-right)

def FindsTheMinDistance(a):
    min=DistanceFinder(a,a[0])
    indexOfMin=0
    for i in range(1, len(a)):
        temp=DistanceFinder(a, a[i])
        if(min>temp):
            min=temp
            indexOfMin=i
    return a[indexOfMin]

