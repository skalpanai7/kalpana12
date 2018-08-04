N,K=map(int,raw_input().split())
list=[int(x) for  x in raw_input().split()]
sum=0
for i in range(0,K):
	sum=sum+list[i]
print(sum)
