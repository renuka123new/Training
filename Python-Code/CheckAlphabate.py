#Write a program to check whether character is an alphabet or not.

data=input("Enter any character you want to enter: ")
status=data.isalpha()
if ((len(data))==1):
    if (status==True):
        print("Entered character is alphabate.")
    else:
        print("Entered character is not an alphabate.")
else:
    print("Please enter character")
