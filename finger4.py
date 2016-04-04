import sys
x=int(sys.argv[1])
i=x-1
while i>1:
	if x%i:i-=1
	else:i=0
print i
