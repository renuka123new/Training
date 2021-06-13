#Program to search given pattern(?=single char and *=multiple char)

#Input:- abcpaqc        pattern:- a?c     output:- abc aqc
#Input:- 1223abcpaqc    pattern:- a*      output:- abcpaqc aqc

def listToString(l1):
    new_str=""
    for i in l1:
        new_str+=i
    return  new_str

str1=input("Enter the string : ")
pattern=input("Enter the pattern you want to search  : ")
str1_len=len(str1)
pattern_len=len(pattern)
flag=0
if(len(str1)>0):
    for i in pattern:
        if(i=='*'):
            flag=1
if(flag==0):
    first=pattern[0]
    last=pattern[pattern_len-1]
    for i in range(len(str1)):
            l=[]
            if(pattern_len==3):
                if(str1[i]==first):
                    if((i+2)<=str1_len):
                        if(str1[i+2]==last):
                            l.append(first)
                            l.append(str1[i+1])
                            l.append(last)
                        else:
                            l.append(first)
                            l.append(str1[i+1])
                if(len(l)>=pattern_len):
                    print(listToString(l),end="\t")

            elif(pattern_len==2):
                if(pattern[0]=='?'):
                    for i in range(str1_len):
                        if(str1[i]==pattern[1]):
                            l.append(str1[i-1])
                            l.append(str1[i])
                            l.append(" ")

                    #if (len(l) >= pattern_len):
                        #print(listToString(l), end="\t")
                else:
                    for i in range(str1_len):
                        if(str1[i]==pattern[0]):
                            l.append(str1[i])
                            if((i+1)<=str1_len):
                                l.append(str1[i + 1])
                            l.append(" ")
    if (len(l) >= pattern_len):
        print(listToString(l))


else:
        if(pattern[1]=='*'):
            l = []
            first = pattern[0]
            for i in range(str1_len):
                if(str1[i]==first):
                    for j in range(i,(str1_len)):
                        #print(j,end=" ")
                        #print(str1[j])
                        l.append(str1[j])
                    l.append(" ")
            print(listToString(l))

        else:
            l = []
            first = pattern[1]
            for i in range(str1_len):
                if(str1[i]==first):
                    for j in range(0,i+1):
                        #print(j,end=" ")
                        #print(str1[j])
                        l.append(str1[j])
                    l.append(" ")
            print(listToString(l))


