#write a python program to print average value in the matrixr,c=int(input()),int(input())
r,c=int(input()),int(input())
l,sum=[],0
for i in range(r):
    l.append(tuple(map(int,input().split())))
for i in l:
    for j in i:
        sum+=j
print(sum/(r*c))


