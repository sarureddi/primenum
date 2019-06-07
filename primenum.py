a11,b1=map(int,input().split())
l1 = list()
for x1 in range(a11,b1+1):
    count1=0
    for i1 in range(1,x1+1):
        if x1%i1==0:
            count1+=1
    if count1==2:
        l1.append(x1)
print(len(l1))
