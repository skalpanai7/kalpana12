n=int(input())
temp=n
l=len(str(n))
sum=0
if(n<=100000):
	while n>0:
		x=n%10
		sum=sum+(x**l)
		n=n/10	
	if(sum==temp):
		print("yes")
	else:
		print("no")
	
