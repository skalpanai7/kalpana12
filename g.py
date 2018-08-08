n,k=map(int,raw_input().split())
for i in range(n,k):
	l=len(str(i))
	sum=0
	temp=i
	while i>0:
		x=i%10
		sum=sum+(x**l)
		i=i/10	
	if(sum==temp):
		print temp,
	
