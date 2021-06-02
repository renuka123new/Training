#write a program to count the number of digits in a given integer

n=int(input("Enter any number:"))
count=0
while(n>0):
    count=count+1
    n=n//10 #// operator gives floor division in python
    #print(n)
print("Number of digits in the given number are:",count)