n=int(input())
temp=n
rev=0
if(n<=1000):
	while(n>0):
		k=n%10
		rev=rev*10+k
		n=n//10
	if(temp==rev):
		print("yes")
		
	else:
		print("no")
