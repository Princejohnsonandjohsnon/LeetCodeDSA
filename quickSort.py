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
print("hello")

"jenkins code "
##!/bin/bash

# Print the workspace and current directory
"""echo "Workspace directory: $WORKSPACE"
echo "Current directory: $(pwd)"
echo "Listing files in workspace:"
ls -l $WORKSPACE

# Execute the Python script directly if it's in the workspace
python quickSort.py"""
