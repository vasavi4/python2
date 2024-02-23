#write a python program to print product of the matrix
r,c=int(input()),int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
#print(l)
product=1
for i in l:
    print(i)
    for j in i:
        product*=j
print(product)
