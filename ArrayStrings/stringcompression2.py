def stringCompression(chars):
    i = 0
    ans = 0
    while i < len(chars):
        j = i + 1
        while j < len(chars) and chars[i] == chars[j]:
            j += 1
        chars[ans] = chars[i]
        ans += 1
        count = j - i
        if count > 1:
            s = str(count)
            for x in s:
                chars[ans] = x
                ans += 1

        i = j
    print('raw chars', chars)
    chars = chars[:ans]
    print('chars',chars)
    print('ans',ans)
    return ans

chars=["a","a","b","b","c","c","c"]

print(stringCompression(chars))