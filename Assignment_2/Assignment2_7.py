def printPattern(no):
    for i in range(1,no+1):
        for j in range(1,no+1):
            print(j,end=" ");
        print();
def main():
    no1 = int(input("Enter The Number: "));
    printPattern(no1);

if __name__ == "__main__":
    main();