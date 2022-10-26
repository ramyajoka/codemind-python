num=int(input())
tem=num
rev=0
while num>0:
    r=num % 10
    rev=rev*10+r
    num=num//10
if tem==rev:
    print('True')
else:
    print('False')