def dryRun():
    arr = ["1","2","3","4","5","6","7" ]
    #arr=[1,2,3,4,5,6,7,8]
    l = ""
    check=[]
    for x in range(14):
        print(x)
        try:
            print("check this out",arr[x])
            if x<9:
                l+=arr[x]
                print("this is array value",arr[x])
            else:
                break

        except:
            print('why this is not running')
            break
    return l


print(dryRun())