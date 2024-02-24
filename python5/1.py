#write a python program to take dictionary as input and print keys and values of a dictionary which is taken at runtime
n=int(input("enter no.of items:"))
d={}
for i in range(n):
    key=input("key:")
    value=input("value:")
    d[key]=value
for i in d:
    print("key:",i,"value:",d[i])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
    
