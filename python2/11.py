#write a python program to removes duplicates in a given string
s=input()
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)
