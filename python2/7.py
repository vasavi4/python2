#write a python program to check whether given number is armstrong number or not
n=int(input())
temp=n
rev=0
while n > 0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev == temp:
    print("armstrong")
else:
    print("not armstrong")
