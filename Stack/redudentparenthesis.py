from sys import *
from collections import *
from math import *

def findRedundantBrackets(s):
	stk = deque()
	for x in range(len(s)):
		if s[x] == '(' or s[x] == '+' or s[x] == '-' or s[x] == '/' or s[x] == '*':
			stk.append(s[x])

		else:
			if s[x] == ')':
				isBool = True
				while stk and stk[-1] != '(':
					if stk[-1] == '+' or stk[-1] == '-' or stk[-1] == '/' or stk[-1] == '*':
						isBool = False
					stk.pop()

				if isBool == True:
					return True
				stk.pop()
	print(stk)
    #print(stk)
	return False


str='(a+b)+(z+b)'
print(findRedundantBrackets(str))