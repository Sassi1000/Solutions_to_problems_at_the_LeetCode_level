
def LargePalindrome(st):
   left=0
   right=len(st)-1
   while(left<len(st) and (ord(st[left])< ord('A') or
                           ord(st[left])> ord('Z'))):
       left+=1
   if(left==len(st)):
       return True
   while(left<right):
       while(right>left and  ( ord(st[right])< ord('A') or
                              ord(st[right])> ord('Z') )):
           right-=1
       if(st[left]!=st[right]):
           return False
       left+=1
       right-=1
   return True
#   3333333A44444A5555555
a="76556SDS78"
print(LargePalindrome(a))
a="76556SD78"
print(LargePalindrome(a))
a="76556S78"
print(LargePalindrome(a))
a="7655678"
print(LargePalindrome(a))




