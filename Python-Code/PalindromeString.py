#code to check whether the given string is palindrome or not
def checkPalindrome(s):
    len1=len(s)
    newstr=s[::-1]
    if(len1>0):
        if (s==newstr):
            print("String is palindrome")
        else:
            print("String is not palindrome")
    else:
        print("Please enter valid string")
    return 0


# main code
s = input("Enter any string you want to check: ")
ans = checkPalindrome(s)


