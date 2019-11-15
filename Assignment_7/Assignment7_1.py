class BookStore():
    noOfBooks=0;
    def __init__(self,name,author):
        self.name = name;
        self.author = author;
        BookStore.noOfBooks = BookStore.noOfBooks + 1;

    def Display(self):
        print("Name is: ",self.name,"Author is: ",self.author," and No of Books is: ",self.noOfBooks);

def main():
    obj1=BookStore("Linux System Programming","Robert Love");
    obj1.Display();
    obj2=BookStore("C Programming","Dennis Ritchie");
    obj2.Display();
    
if __name__ == "__main__":
    main();
