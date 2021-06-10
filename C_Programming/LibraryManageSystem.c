#define _CRT_SECURE_NO_WARNINGS 1
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
typedef struct Node{
	int id;
    char book_name[20];
    int cost;
    char auther[30];
}Node;
typedef struct Book{
	Node date;
	struct Book*next;
}book;
book*GreatLink()
{
	book*h, *tail, *p;
	h=tail=(book*)malloc(sizeof(book));
	h->next = NULL;
	int n = 0;
	printf("Enter the number of books to be entered:");
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		p = (book*)malloc(sizeof(book));
        printf("Book Id:");
		scanf("%d",&p->date.id);
		printf("Book Title:");
		scanf("%s",&p->date.book_name);
		printf("Auther:");
		scanf("%s",&p->date.auther);
		printf("price:");
		scanf("%d",&p->date.cost);
		p->next = NULL;
		tail->next = p; 
		tail = p;
	}

	return h;
}
void Insert(book*h)// insert (head insertion method)
{
	book*p;
		p = (book*)malloc(sizeof(book));
		printf("Book Id:");
		scanf("%d",&p->date.id);
		printf("Book Title:");
		scanf("%s",&p->date.book_name);
		printf("Auther:");
		scanf("%s",&p->date.auther);
		printf("price:");
		scanf("%d",&p->date.cost);
		p->next = h->next;
		h->next = p;
	
}
void Search1(book*h)// Book title search
{
	char name[20];
	book*p = h->next;
	printf("Enter the title you want to find:");
	scanf("%s",&name);
	while (p!=NULL)
	{
		if (strcmp(p->date.book_name,name)!=0)
		{
			p = p->next;
		}
		else 
		{
			printf("Book Id \t Book Title \t Auther \t Price \n");
			printf("%d\t%s\t%s\t%d\n",p->date.id,p->date.book_name,p->date.auther,p->date.cost);
			return;
		}
	}
	if (p == NULL)
	{
		printf("Not found! \n");
	}
}
void Search2(book*h)// Auther search
{
	char auther[20];
	book*p = h->next;
	printf("Enter the Auther to find:");
	scanf("%s", &auther);
	while (p != NULL)
	{
		if (strcmp(p->date.auther, auther)!=0)
		{
			p = p->next;
		}
		else
		{
			printf("Book Id \t Book Title \t Auther \t Price \n");
			printf("%d\t%s\t%s\t%d\n", p->date.id,p->date.book_name, p->date.auther, p->date.cost);
			return;
		}
	}
	if (p == NULL)
	{
		printf("Not found! \n");
	}
}
void PrintLink(book*h)// output
{
	book*p;
	printf("Book_Id \t Book_Title \t Auther \t Price \n");
	for (p = h->next; p != NULL; p = p->next)
	{
        printf("%d\t",p->date.id);
		printf("%s\t",p->date.book_name);
		printf("%s\t", p->date.auther);
		printf("%d\t", p->date.cost);
		printf("\n");
	}

}
void delete(book*h)
{
	char auther[20];// Delete by Auther 
	book*p = h->next;
	book*tail = h;
	printf("Enter the auther of the book to be deleted:");
	scanf("%s", &auther);
	while (p != NULL)
	{
		if (strcmp(p->date.auther, auther)!=0)
		{
			p = p->next;
			tail = tail->next;
		}
		else
		{
			tail->next = p->next;
			free(p);
			return;
		}
	}
}
void menu()
{
	printf("\n--------- Welcome to Online Library Management System --------- \n");
	printf("1. To create new system \n");
	printf("2. To insert new book \n");
	printf("3. To search book by title\n");
	printf("4. To search book by Auther \n");
	printf("5. To delete book from system \n");
	printf("6. To print list of books \n");
	printf("Note: Only enter once, otherwise it will overwrite \n");
}
void choose(book*h)
{
	int i;
	int a = 1;

	while (a>0)
	{
		menu();
		printf("please enter your choice:");
		scanf("%d",&i);
		switch (i)
		{
		case 1:
			h=GreatLink();
			break;
		case 2:
			Insert(h);
			break;
		case 3:
			Search1(h);
			break;
		case 4:
				Search2(h);
				break;
		case 5:
				delete(h);
				break;
		case 6:
				PrintLink(h);
				break;
		default:
			printf("Invalid choice! \n");
				a = -1;// jump out of the loop condition 
				break;
			}
		}
}

int main()
{
	book*head = NULL;
	choose(head);
	return 0;
}
