from database import load,save
from datetime import datetime

B_FILE ="books.json"
S_FILE ="students.json"
I_FILE ="issued_books.json"

def add_book():
  books = load(B_FILE)
  books = [b for b in books if isinstance(b, dict)]

  bid = input("Book ID: ")

  if any(b.get("book_id", "").lower() == bid.lower() for b in books):
     print("Error: Book ID already exists.")
     return
  title = input("Book Name: ")
  author = input("Author Name: ")
  category = input("Category: ")
  copies_str = input("Total Copies: ")

  if copies_str.isdigit():
    copies = int(copies_str)
    if copies <= 0:
      return print("Error: Copies must be greater than 0.")
  else:
    return print("Error: Enter a valid number.")

  books.append({
      "book_id": bid,
      "book_name": title,
      "author": author,
      "category": category,
      "available_copies": copies,
  })
  save(B_FILE, books)
  print("Success: Book added successfully!")

#module 2: Display All books
def display_books():
  books = [b for b in load(B_FILE) if isinstance(b, dict)]

  if not books:
     print("No books available.")
     return
  print(
      f"{'ID':<10} | {'Book Name':<20} | {'Author':<15} | {'Category':<12} |"
      f" {'Copies':<6}"
  )
  print("-" * 72)
  for b in books:
    print(
        f"{str(b.get('book_id', '')):<10} |"
        f" {str(b.get('book_name', '')):<20} |"
        f" {str(b.get('author', '')):<15} |"
        f" {str(b.get('category', '')):<12} |"
        f" {b.get('available_copies', 0)}"
    )
#module 3: Search book
def search_book():
    books = load(B_FILE)
    if not books:
         print("books are not available:")
         return
    q = input("Search by ID, Name, Author: ").lower()
    res = [
        b 
        for b in books
        if q in b["book_id"].lower()
        or q in b["book_name"].lower()
        or q in b["author"].lower()
    ]
    for b in res:
        print(
            f"ID:{b['book_id']} |Name:{b['book_name']} | Author:{b['author']} | Copies:{b['available_copies']}"
        )
    if not res:
        print("NO Matching books found")    

 #module 4: Register student    
def register_student():
     student = load(S_FILE)
     sid = input("student ID:")
     if any(s["student_id"].lower() == sid.lower() for s in student):
         print("Error:Student ID already Exist")
         return
     student.append({
         "student_id":sid,
         "student_name":input("student name:"),
         "department":input("Department:"),
         "Contact":input("Contact:")
     })
     save(S_FILE,student)
     print("Success: student register")
     
 #module 5: issue book
def issue_book():
      issue = load(I_FILE)
      student = load(S_FILE)
      book = load(B_FILE)
      
      sid = input("student ID:")
      bid = input("Book ID:")
      
      if not any(s["student_id"].lower() == sid.lower() for s in student):
             print("Error:Student ID not register")
             return
      book =next((b for b in book if b["book_id"].lower() == bid.lower()),None) 
      if not book or book ["available_copies"] <= 0:
          print("Error: book are not available or invalid ID")
          return
      issue.append(
          {"student_id":sid,"bid_id":bid,"date":datetime.now().strftime("%x")}
      )
      save(B_FILE,book)
      save(I_FILE,issue)
      print("success:Book issusd successfully")

#module:6 return book
def return_book():
  books = [b for b in load(B_FILE) if isinstance(b, dict)]
  issued = [i for i in load(I_FILE) if isinstance(i, dict)]

  sid = input("Student ID: ")
  bid = input("Book ID: ")

  rec = next(
      (
          i
          for i in issued
          if str(i.get("student_id", "")).lower() == sid.lower()
          and str(i.get("book_id") or i.get("bid_id", "")).lower()
          == bid.lower()
      ),
      None,
  )

  if not rec:
    return print("Error: Active issue record not found.")

  issued.remove(rec)

  for b in books:
    if str(b.get("book_id") or b.get("bid_id", "")).lower() == bid.lower():
      b["available_copies"] = int(b.get("available_copies", 0)) + 1
      break
  else:
    books.append({"book_id": bid, "available_copies": 1})

  save(B_FILE, books)
  save(I_FILE, issued)
  print("Success: Book returned successfully") 

#module:7 issue list 
def display_issued():
  issued = [i for i in load(I_FILE) if isinstance(i, dict)]
  if not issued:
     print("No books are currently issued.")
     return
  print(f"{'Student ID':<15} | {'Book ID':<10} | {'Date':<12}")
  print("-" * 42)
  for i in issued:
    b_id = i.get("book_id") or i.get("bid_id") or i.get("bid", "")
    print(
        f"{str(i.get('student_id', '')):<15} | {str(b_id):<10} |"
        f" {str(i.get('date', '')):<12}"
    )
    save(I_FILE,issued)

#module:8 delete books
def delete_book():
  books = [b for b in load(B_FILE) if isinstance(b, dict)]
  issued = [i for i in load(I_FILE) if isinstance(i, dict)]

  bid = input("Enter book ID to delete: ").strip()

  if any(
      (i.get("book_id") or i.get("bid_id") or "").lower() == bid.lower()
      for i in issued
  ):
     print("Error: Cannot delete, book is currently issued.")
     return
  if not any(
      (b.get("book_id") or b.get("bid_id") or "").lower() == bid.lower()
      for b in books
  ):
    return print("Error: Book ID not found.")

  books = [
      b
      for b in books
      if b.get("book_id","").lower() != bid.lower()
  ]
  save(B_FILE, books)
  print("Success: Book deleted successfully")
    