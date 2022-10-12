a=input()
f=a[0]
l=0
for i in range(len(a))[::-1]:
    if a[i]==f:
        l=i
        break
if l==0:
    print(0)
else:
    print(l-1)
