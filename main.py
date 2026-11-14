from All_function import (
    add_book,
    display_books,
    search_book,
    register_student,
    issue_book,
    return_book,
    display_issued,
    delete_book
)
def main():
    while True:
        print(
            "\n---Library Menu-----\n1.Add Book 2.display all book 3.search book 4.register student \n5.Issuse book 6.return book 7.issued list 8.delete book 9.Exit"
        )        
        user = input("Enter choice (1-9):")
        if user == "1":
             add_book()
        elif user =="2":
           display_books() 
        elif user == "3":
            search_book() 
        elif user == "4":
           register_student()
        elif user == "5":
           issue_book()  
        elif user == "6":
            return_book()
        elif user =="7":
            display_issued()    
        elif user == "8":
           delete_book()
        elif user == "9": 
           print("Thank you for visiting")
           break
        else:
            print("Invalid choices")
        
           
main()            