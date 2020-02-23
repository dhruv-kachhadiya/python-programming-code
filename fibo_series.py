def fibo(n):
    f=0
    s=1
    if(n==1):
        print(f)
    elif(n==2):
        print(s)
    else:
        print(f,'\n',s)
        count=2
        
        while(count<n):
         next=f+s
         f=s
         s=next
         print(next)
         count += 1

n=int(input('enter total number that you want to print :'))
print(f'\n\nfibonaki series upto {n} numbers :')
fibo(n)

