class Library():
    def __init__(self, list_of_books, library_name):
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = library_name

        for books in self.list_of_books:
            self.lend_data[books] = None

            
    def display_book(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index} {books}")


    def lend_book(self, book_name, author):
        if book_name in self.list_of_books:
            if self.lend_data[book_name] is None:
                self.lend_data[book_name] = author
            else:
                print(f"Sorry the book you have entered is not in the library its been taken by {self.lend_data[book_name]}")
        else:
            print("Please Enter A valid book name!")


    def add_book(self, book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None


    def return_book(self, book_name, author):
        if book_name in self.list_of_books:
            if self.lend_data[book_name] is not None:
                self.lend_data.pop(book_name)
            else:
                print("sorry this book is not lended by any one!")
        else: 
            print("you have entered a invalid book name!")


    def delete_book(self, book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)



def main():
    list_books = ['Cookbook','Motu Patlu','Chacha_chaudhary','Rich Dad and Poor Dad']
    Library_name = 'Harry'
    secret_key = 123456

    Harry = Library(list_books, Library_name)

    print(f"Welcome to Library of {Harry.library_name} \n\n Display Books Using 'D'\n Lend Book Using 'L'\n Add Book Using 'A'\n Return Book Using 'R'\n Delete Book using 'Del'\n Exit Using  'E'\n\n" )

    Exit = False
    while(Exit is not True):
        _input1 = input("Option:")
        print('\n')

        if _input1 == 'D' or _input1 == 'd':
            Harry.display_book()

        elif _input1 == 'L'  or _input1 == 'l':
            _Author = input("Enter your name :")
            _Book_name = input("Enter Book Name :")
            print("-----Book Lend-----")
            Harry.lend_book(_Book_name, _Author)

        elif _input1 == 'A' or _input1 == 'a':
            _Book_name = input("Enter Book Name :")
            print("-----Adding Book-----")
            Harry.add_book(_Book_name)

        elif _input1 == 'R' or _input1 == 'r':
            _Author = input("Enter your name :")
            _Book_name = input("Enter Book Name :")
            Harry.return_book(_Book_name, _Author)
        
        elif _input1 == 'Del' or _input1 == 'del':
            _Book_name = input("Enter Book Name you Want to Delete :")
            _key = int(input("Enter the Secrate Key :"))

            if _key == secret_key:
                Harry.delete_book(_Book_name)
                print("-----Book Deleted-----")
            else:
                print("Sorry your Secrate Key is not Right")
        elif _input1 == 'E' or _input1 == 'e':
            Exit = True

if __name__ == "__main__":
    main()

