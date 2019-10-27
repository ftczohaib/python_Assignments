def printPattern(no):
    for i in range(no):
        for j in range(no):
            print("*",end="");
        print();
def main():
    no1 = int(input("Enter The Number: "));
    printPattern(no1);

if __name__ == "__main__":
    main();