x,y,z=map(int,raw_input().split())

if(x>=y and x>=z):
	l=x
elif(y>=x and y>=z):
	l=y
else:
	l=z
print(l)
