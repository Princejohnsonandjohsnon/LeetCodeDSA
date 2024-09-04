from collections import deque

def solve(inputStack,count,N):
    print('inputStack',inputStack)
    print('count',count,len(inputStack)//2)
    if count==N//2:
        inputStack.pop()
        print('wy',inputStack)
        return

    popValue=inputStack[-1]
    inputStack.pop()
    count+=1
    solve(inputStack,count,N)
    inputStack.append(popValue)
    #print(inputStack)

def deleteMiddle(inputStack, N):

    # Write your solution here
    inputStack=deque(inputStack)
    count=0
    solve(inputStack,count,N)
    return inputStack


inputStack=[1,2,3,4,5]
N=len(inputStack)
print(deleteMiddle(inputStack,N))
