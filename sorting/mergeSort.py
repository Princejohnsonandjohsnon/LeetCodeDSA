def sort(stack,firstHalf,seconfHalf):
    print('stack is what',stack)
    print('firstHalf',firstHalf)
    print('secondHalf',seconfHalf)
    totalIndex=len(firstHalf)+len(seconfHalf)-1
    i=len(firstHalf)-1
    j=len(seconfHalf)-1
    while i>=0 and j>=0:
        if firstHalf[i]>=seconfHalf[j]:
            stack[totalIndex]=firstHalf[i]
            i-=1
            totalIndex -= 1
        elif seconfHalf[j]>firstHalf[i]:
            stack[totalIndex]=seconfHalf[j]
            j-=1
            totalIndex -= 1


    if i>=0:
        while i>=0:
            stack[totalIndex]=firstHalf[i]
            i-=1
            totalIndex-=1
    if j>=0:
        while j>=0:
            stack[totalIndex]=seconfHalf[j]
            j-=1
            totalIndex-=1
    print('stack after each merge and sort',stack)
    return stack



def merge(stack):
    print('stack',stack)

    if len(stack)==1:
        return stack
    half=len(stack)//2
    firstHalf=merge(stack[:half])
    print('firstHald merge loop',firstHalf)
    secondHalf=merge(stack[half:])
    print('secondhalf merge loop', secondHalf)
    return sort(stack,firstHalf,secondHalf)


def ans(stack):
    firstHalf=[]
    secondHalf=[]
    stack=merge(stack)
    return stack


stack=[5,-2,9,-7,3]
print(ans(stack))