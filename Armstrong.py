num=int(input("Please enter the number to be checked"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
print(sum)
print(num)
if sum==num:
    print("the number is an armstrong number")
else:
    print("it is not an armstrong")