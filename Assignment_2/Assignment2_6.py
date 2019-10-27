def printPattern(no):
    for i in range(no,0,-1):
        no1=i;
        for j in range(no1):
            print("*",end=" ");
        print();
def main():
    no1 = int(input("Enter The Number: "));
    printPattern(no1);

if __name__ == "__main__":
    main();