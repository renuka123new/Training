#program to evaluate reverse polish notation
expression=input("Please enter space seperated inputs: ")
l1=[]
num=[]
operator=[]
str1=expression.split(" ")

for i in str1:
    if(i.isdigit()):
        num.append(i)
    elif(i=='+' or i=='-' or i=='*' or i=='/' or i=='%'):
        operator.append(i)
print(num)
print(operator)
n,op,ans=0,0,0

if(operator[op]=='+'):
    ans=int(num[n])+int(num[(n+1)])
elif(operator[op]=='-'):
    ans=int(num[n])-int(num[n+1])
elif(operator[op]=='*'):
    ans=int(num[n])*int(num[n+1])
else:
    ans=int(num[n])/int(num[n+1])
n,op=2,1
while(n<len(num)):
    if(operator[op]=='+'):
        ans=ans+int(num[n])
    elif(operator[op]=='-'):
        ans=ans-int(num[n])
    elif(operator[op]=='*'):
        ans=ans*int(num[n])
    elif (operator[op] == '/'):
        ans = ans / int(num[n])
    else:
        ans=ans%int(num[n])
    n=n+1
    op=op+1
print(ans)