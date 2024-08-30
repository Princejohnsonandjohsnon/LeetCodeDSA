from collections import Counter
def close(word1,word2):
    ch1=Counter(word1)
    ch2=Counter(word2)
    n1=Counter([v for v in ch1.values()])
    n2=Counter ([v for v in ch2.values()])
    print(n1,n2)
    return n1==n2


word1='abcc'
word2='bcacc'
print(close(word1,word2))
