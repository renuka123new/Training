def word_length_1(num):
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    print(num, ":", end=" ")
    print(single_digits[ord(num[0]) - 48])
    return

def word_length_2(num):
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    two_digits = ["", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
    tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]

    x = 0
    while (x < len(num)):

        if (ord(num[x]) - 48 == 1):
            sum = (ord(num[x]) - 48 +
                    ord(num[x + 1]) - 48)
            print(two_digits[sum])
            return

        elif (ord(num[x]) - 48 == 2 and
                              ord(num[x + 1]) - 48 == 0):
            print("twenty")
            return


        else:
            i = ord(num[x]) - 48
            if (i > 0):
                print(tens_multiple[i], end=" ")
            else:
                print("", end="")
            x += 1
            if (ord(num[x]) - 48 != 0):
                print(single_digits[ord(num[x]) - 48])


        x += 1

# main Code
n=input("Enter any number upto 2 digit: ")

l = len(n)
if (l == 0):
    print("empty string")
if(l==1):
    word_length_1(n) # number up to 1 digit
elif(l==2):
    word_length_2(n)  # number up to 2 digit


else:
    print("Length more than 2 is not supported")