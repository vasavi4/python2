#write a python program to print whether given element is enagram or not
s1,s2=map(str,input().split())
if len(s1) == len(s2):
    if sorted(list(s1)) == sorted(list(s2)):
        print(sorted(list(s1)))
        print(sorted(list(s2)))
        print(True)
    else:
        print(False)
else:
    print(False)
    
