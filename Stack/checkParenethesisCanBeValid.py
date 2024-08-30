class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        stk = deque()
        if len(s) % 2 != 0:
            return False
        for x, y in enumerate(s):
            if s[x] == '(' and locked[x] == 0:
                stk.append(x)
            elif s[x] == ')':
                if stk and s[stk[-1]] == '(':
                    stk.pop()
                elif locked[x] == '0':
                    stk.append(x)
        print(stk)

        return True

