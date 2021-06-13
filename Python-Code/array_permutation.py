#Code to write all permutation of given user_input

def listToString(l1):
	new_str = ""
	for i in l1:
		new_str += i
	return new_str

def permute(input_string, start, end):
	if start==end:
		print (listToString(input_string))
	else:
		for i in range(start,end+1):
			input_string[start], input_string[i] = input_string[i], input_string[start]
			permute(input_string, start+1, end)
			input_string[start], input_string[i] = input_string[i], input_string[start] # backtrack

user_string=input("Enter any string : ")
user_string_len = len(user_string)
user_string_list = list(user_string)
permute(user_string_list, 0, user_string_len-1)

