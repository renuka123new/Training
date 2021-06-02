#Find total occurrences of each digits (0-9) using function.
def countOcc(n):
    l = []
    while (n >= 1):
        reminder = int(n % 10)
        n = n / 10
        l.append(reminder)
    for i in range(0, 10):
        count = 0
        for j in l:
            if (i == j):
                count = count + 1
        print("Count of ", i, " = ", count)
num=int(input("Enter any number: "))
countOcc(num)
