#code to calculate word frequency
user_Input=input("Enter the string")
special_Char="*@,.()/\[]1234567890"
for i in special_Char:
    user_Input=user_Input.replace(i,"")
#print(user_Input)
convert_string_list=user_Input.split(" ")
remove_duplicate=[]
for i in convert_string_list:
    if i not in remove_duplicate:
        remove_duplicate.append(i)
l1=len(convert_string_list)
for i in remove_duplicate:
    count=0
    for j in convert_string_list:
        if(i==j):
            count=count+1
    print(i,"=",count)
