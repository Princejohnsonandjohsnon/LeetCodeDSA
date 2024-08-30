def reverse(z):
    ans=z
    value=0
    while ans!=0:
        rem=ans%10
        value=value*10+rem
        print('value',value)
        ans=ans//10
    return value

z=123
print(reverse(z))