#prime number or not
n=int(input())
for i in range(2,(n**0.5)+1):
    if n%i==0:
       print("not a prime")
       break
else:
    print("prime")

        
        
    
