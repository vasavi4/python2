#write a python program to check whether the given number is strong number or not by using string or recursion
def fact(n):
    if n<1:
        return 1
    else:
        return n*fact(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=fact(int(i))
    if sum == x:
        return "strong number"
    else:
        return "not strong number"
x=int(input())
print(strong(x))

