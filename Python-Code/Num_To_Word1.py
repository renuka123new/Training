def split_string(num):
    l=[]
    len_word=len(num)
    for i in range(len_word):
        l.append(num[i])
    return l
def word_length_1(num):
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    #print(num, ":", end=" ")
    print(single_digits[ord(num[0]) - 48],end=" ")
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
            print(two_digits[sum],end=" ")
            return

        elif (ord(num[x]) - 48 == 2 and
                              ord(num[x + 1]) - 48 == 0):
            print("twenty",end=" ")
            return


        else:
            i = ord(num[x]) - 48
            if (i > 0):
                print(tens_multiple[i], end=" ")
            else:
                print("", end="")
            x += 1
            if (ord(num[x]) - 48 != 0):
                print(single_digits[ord(num[x]) - 48],end=" ")


        x += 1

def word_length_3(num):
    list_3=split_string(num)
    first_digit=list_3[0]
    word_length_1(first_digit)
    print("hundred",end=" ")
    last_two_digit=list_3[1]+list_3[2]
    word_length_2(last_two_digit)

def word_length_4(num):
    list_4=split_string(num)
    first_digit=list_4[0]
    if(int(first_digit)!=0):
        word_length_1(first_digit)
        print("thousand", end=" ")
    second_digit=list_4[1]
    if(int(second_digit)!=0):
        word_length_1(second_digit)
        print("hundred", end=" ")
    last_two_digit = list_4[2] + list_4[3]
    if(last_two_digit!=0):
        word_length_2(last_two_digit)

def word_length_5(num):
    list_5 = split_string(num)
    first_Two_digit = list_5[0]+list_5[1]
    if(int(first_Two_digit)!=0):
        word_length_2(first_Two_digit)
        print("thousand", end=" ")
    second_digit = list_5[2]
    if (int(second_digit) != 0):
        word_length_1(second_digit)
        print("hundred", end=" ")
    last_two_digit = list_5[3] + list_5[4]
    if (last_two_digit != 0):
        word_length_2(last_two_digit)

def word_length_6(num):
    list_6 = split_string(num)
    first_digit=list_6[0]
    word_length_1(first_digit)
    print("lakh", end=" ")
    remaining_digits=list_6[1]+list_6[2]+list_6[3]+list_6[4]+list_6[5]
    if (int(remaining_digits) != 0):
        word_length_5(remaining_digits)

def word_length_7(num):
    list_7=split_string(num)
    first_Two_digit = list_7[0] + list_7[1]
    word_length_2(first_Two_digit)
    print("lakh", end=" ")
    remaining_digits = list_7[2] + list_7[3] + list_7[4] + list_7[5] + list_7[6]
    if (int(remaining_digits) != 0):
        word_length_5(remaining_digits)


# main Code
n=input("Enter any number upto 7 digit: ")

l = len(n)
if (l == 0):
    print("empty string")
if(l==1):
    word_length_1(n) # number up to 1 digit
elif(l==2):
    word_length_2(n)  # number up to 2 digit
elif(l==3):
    word_length_3(n)  # number up to 3 digit
elif(l==4):
    word_length_4(n)  # number up to 4 digit
elif(l==5):
    word_length_5(n)  # number up to 5 digit
elif(l==6):
    word_length_6(n)  # number up to 5 digit
elif(l==7):
    word_length_7(n)  # number up to 5 digit

else:
    print("Length more than 7 is not supported")
#Similarly we can write for number of any length