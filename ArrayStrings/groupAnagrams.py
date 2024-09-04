from collections import defaultdict
def groupAnagrams(strs):
    d = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for x in s:
            charOrd = ord(x) - ord('a')
            count[charOrd] += 1
        print(count)

        d[tuple(count)].append(s)
    print(d)
    return d.values()

strs=["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))