n=int(input("Enter a Number:"))
sum=0
for i in range(1,n):
  if(n%i==0):
   sum=sum+i
print(sum)
if(n==sum):
    print("Number is Perfect Number")
else:
    print("Number is Imperfect Number")
