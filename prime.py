n = int(input())
i = 2
flag = True
while i<=n:
  if n%i==0:
    flag=False
    break
  i+=1 # i=i+1

if flag:
  print('prime number')
else:
  print('not a prime number')
  
    
