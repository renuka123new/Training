library = {}

def searchbook(search_id):
    if search_id in library.keys():
        return library[search_id]
    else:
        return None

flag = True
while flag:
    print("\n********* WEL-COME TO ONLINE LIBRARY *********\n1.Insert Book\n2.list all books\n3.search book\n4.delete book \n5.exit\n")
    ch = int(input("Enter Your Choice: "))
    if ch == 1:
        n=int(input("Enter the numner of book you want to enter: "))
        for i in range(n):
            book_id = int(input("Enter Id of Book:"))
            book_name = input("Enter title of Book:")
            book_author = input("Enter author of book:")
            book_cost = float(input("Enter price of Book:"))
            library[book_id] = [book_name,book_cost, book_author]
    elif ch == 2:
        print("\n")
        for key, value in library.items():
            print("Book Id:{}".format(key))
            print("Book name:{}".format(value[0]))
            print("Book Author:{}".format(value[2]))
            print("Book Cost:{}".format(value[1]))
            print("---------------")
    elif ch == 3:
        print("Please enter id of book u want to search:")
        searchBook = int(input())
        searchresult = searchbook(searchBook)
        if searchresult == None:
            print("Book Not found\n")
        else:
            print("\n Book found Successfully")
            print("Book Id:{}".format(searchBook))
            print("Book name:{}".format(searchresult[0]))
            print("Book Author:{}".format(searchresult[2]))
            print("Book Cost:{}".format(searchresult[1]))
    elif ch == 4:
        print("Please enter id of book u want to delete:")
        deleteBook = int(input())
        if deleteBook in library.keys():
            library.pop(deleteBook)
            print("Book is removed from library...!!\n")
        else:
            print("\n Invalid book ID...!!")

    else:
        flag=False
