class Library:

    def __init__(self):

        self.books=[]


    def add_book(self,book):

        self.books.append(
            {
                "name":book,
                "available":True
            }
        )

        print("Book added.")


    def view_books(self):

        if not self.books:

            print("No books available.")

            return

        print("\nBooks:\n")

        for index,book in enumerate(
            self.books,
            start=1
        ):

            status=(
                "Available"
                if book["available"]
                else
                "Borrowed"
            )

            print(
                f"{index}. {book['name']} - {status}"
            )


    def borrow_book(self,name):

        for book in self.books:

            if (
                book["name"].lower()
                ==
                name.lower()
            ):

                if book["available"]:

                    book["available"]=False

                    print("Book borrowed.")

                else:

                    print("Book already borrowed.")

                return

        print("Book not found.")


    def return_book(self,name):

        for book in self.books:

            if (
                book["name"].lower()
                ==
                name.lower()
            ):

                book["available"]=True

                print("Book returned.")

                return

        print("Book not found.")


library=Library()


while True:

    print("\nLibrary System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice=input("\nEnter choice: ")

    if choice=="1":

        book=input("Enter book name: ")

        library.add_book(book)

    elif choice=="2":

        library.view_books()

    elif choice=="3":

        name=input(
            "Enter book to borrow: "
        )

        library.borrow_book(name)

    elif choice=="4":

        name=input(
            "Enter book to return: "
        )

        library.return_book(name)

    elif choice=="5":

        print("Exiting...")

        break

    else:

        print("Invalid choice.")