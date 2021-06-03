#perfectDivisor on Hackerearth
"""You are given a positive integer X and your task is to find the summation of its perfect square divisors.
sample Input
2   (no. of testcase)
2 2
3 1

Explanation
the sampe input corresponds to X = 2^2 * 3^1 = 12, which has these divisors : 1, 2, 3, 4, 6, 12.
Among these divisors these are pefect square : 1, 4, so the answer is 1 + 4 = 5

output :-  5
"""
t=int(input("Enter the number of test cases : "))
t1=[]
result=[]
divisors=[]
square=[]
def sum(newlist):
    r=0
    for x in newlist:
        r=r+x
    return r
def multi(myList):
    r=1
    for x in myList:
        r=r*x
    return r
def divisor(n):
    i=1
    d=[]
    while i<=n:
        if(n%i == 0):
            d.append(i)
        i=i+1
    return d
if(1<=t<=100000):
    for i in range(t):
        test=input("Enter the test case : ")
        #print(test)
        t1=test.split(" ")
        #print(t1)
        t3=[]
        for i in t1:
            a=int(i)
            t3.append(a)
        if(1<=t3[0],t3[1]<=2000000):
            #print(t3)
            m=t3[0]**t3[1]
            result.append(m)
            q=multi(result)
            #print(q)
    divisors=divisor(q)
    for i in range(len(divisors)):
        if((i**(.5))==int(i**(.5))):
            square.append(i)
    sum1=sum(square)
    print(sum1)