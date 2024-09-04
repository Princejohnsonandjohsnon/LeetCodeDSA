from os import *
from sys import *
from collections import *
from math import *

def findMinimumCost(str):
	# Write your code here.
	if len(str)%2!=0:
		return -1
	stk=deque()
	count=0
	for x in range(len(str)):
		if str[x]=='{':
			stk.append(str[x])
		else:

			if stk and str[x]=='}':
				stk.pop()
			else:
				count += 1
	print('stk is ',stk)
	ans=len(stk)//2
	rem=len(stk)%2
	print('count is',count)
	countRem=0
	if count>1:
		countRem = count % 2
		count=count//2

	ans=ans+rem+count+countRem
	return ans

#s='}{{}}}'
s='}}}{{{'
print(findMinimumCost(s))