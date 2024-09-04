def ans(chars):
    d=dict()
    for x in chars:
        if x in d:
            d[x]+=1
        else:
            d[x]=1
    print(d)
    count=0
    l=[]
    for k,v in d.items():
        if d[k]>1 and d[k]<10:
            print('key is ',k)
            l.append(str(k))
            l.append(d[k])
            count+=2
        if d[k]==1:
            print('key is ', str(k))
            l.append(str(k))
            count+=1
        if d[k]>=10:
            print('key is ', k)
            l.append(str(k))
            count+=1
            val=d[k]
            ans=val
            val1=0
            while ans!=0:
                rem=ans % 10
                val1=val1*10+rem
                ans=ans//10
            val2=0
            while val1!=0:
                rem= val1%10
                val2=val2*10+ rem
                l.append(str(rem))
                val1=val1//10

    return l
chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(ans(chars))