#nested dict
l,d=map(int,input().split())
lst=list(map(int,input().split()))
for i in lst:
    for j in lst:
         if i-j == d:
            flag=1
if flag==0:
    print(True)
else:
    print(False)
