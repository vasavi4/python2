#write a python program to check whether the given number is strong number or not using functions
def strongnumber(n,m):
    for i in range(n,m+1):
       x,sum=i,0
       while i>0:
          digit=i%10
          fact=1
          for j in range(1,digit+1):
           fact*=j
          sum+=fact
          i//=10
       if sum==x:
          print(x)
n,m=int(input()),int(input())
strongnumber(n,m)
         
     
     
