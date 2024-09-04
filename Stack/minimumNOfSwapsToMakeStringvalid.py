from collections import deque


def minSwaps(s):
    stk = deque()
    count = 0

    for x in range(len(s)):
        if s[x] == '[':
            stk.append(s)
        else:
            if stk and s[x] == ']':
                stk.pop
            else:
                count += 1

    ans = len(stk) // 2
    rem = len(stk) % 2
    print('count is', count)
    countRem = 0
    if count > 1:
        countRem = count % 2
        count = count // 2

    ans = ans + rem + count + countRem
    return ans//2

    # s='}{{}}}'
s = '[]'
print(minSwaps(s))