def AcceptData():
    return int(input("Enter the Number to Print : "));

def PrintPatternInRecursion(size):
    if size != 0:
        print(size,end=" ")
        size = (size - 1);
        PrintPatternInRecursion(size);

def main():
    size = AcceptData();
    PrintPatternInRecursion(size);

if __name__ =="__main__":
    main();