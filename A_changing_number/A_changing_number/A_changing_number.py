def A_changing_number(f):
    if(f<10):
        return True
    while(f>9):
        if(f%2==(f//10)%2):
            return False
        f=f//10
    return True        

def Min_index_of_a_variable_number(a):
    min=111111111
    indexMin=-1
    for i in range(len(a)):
        if(A_changing_number(a[i])):
            sum=0
            temp=a[i]
            while(temp>0):
                sum+=temp%10
                temp=temp//10
            if(min>sum):
                min=sum
                indexMin=i
    return indexMin

#### MAIN ####

a=12345
print(A_changing_number(a))

a=[66,123,1,77,12]
print(Min_index_of_a_variable_number(a))
    
    
