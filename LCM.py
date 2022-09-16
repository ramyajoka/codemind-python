num1,num2=map(int,input().split())
if(num1 > num2 ):   # Use If condition to find the greatest number among these two.
    max= num1
else:
    max= num2
while(True):
    if(max % num1 == 0 and max % num2 == 0):   
        print(max)
        break;
    max= max+ 1