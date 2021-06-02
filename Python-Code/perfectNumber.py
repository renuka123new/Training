#Write a program to print all Perfect numbers between 1 to n.
def perfectNum(begin, end):
    for i in range(begin, end + 1):
        sum1 = 0
        for x in range(1, i):
            if(i % x == 0):
                sum1 = sum1 + x
        if (sum1 == i):
            print(i)
n=int(input("Enter the upper limit: "))
perfectNum(1, n)