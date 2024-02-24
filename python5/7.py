#write a python program to find repeating character
s=input()
for i in s:
    if s.count(i)>1:
        print(i)
        break
else:
    print('.')
