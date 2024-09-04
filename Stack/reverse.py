from collections import deque

def reverse(stk):
    ans=deque()
    i,j=0,len(stk)-1
    while i<=j:
        stk[i],stk[j]=stk[j],stk[i]
        i+=1
        j-=1
    return stk


s='prince'
stk=deque(list(s))
print(reverse(stk))