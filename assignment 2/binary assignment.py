n=int(input("enter the decimal value\n"))
bs=''
while n !=0:
  bs=bs+str(n%2)
  n=n//2
print("decial equal binary number is ")
for i in range(len(bs)-1,-1,-1):
  print(bs[i],end='')  
