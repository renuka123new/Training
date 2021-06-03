"""Problem
A love Guru determines "whether a guy's proposal is going to be accepted by his crush or not" just by doing some mysterious calculation on
their names, but it takes too much time for him. So, he hired you as a programmer and now your task is to write a program that helps the Guru.
He reveals his mystery with you and that is:
If the guy's name is a subsequence of his crush's name, then she is going to accept him, otherwise she will reject him.

Input

First line contains T, the number of test cases.
Next T lines contain two strings S1 and S2 which are the guy's name and his crush's name respectively.

Output

For each test case, according to Guru's mystery, if the crush is going to accept the guy then print "Love you too", otherwise
print "We are only friends"."""
def subString(str1, str2):
    m=len(str1)
    n=len(str2)

    j=0
    i=0

    while j<m and i<n:
        if str1[j] == str2[i]:
            j=j+1
        i=i+1
    return  j==m

n=int(input("Enter the no. of test case : "))
for i in range(n):
    str1=input("str1: ")
    str2=input("str2: ")

    if subString(str1, str2):
        print("Love you too")
    else:
        print("We are only friends")
