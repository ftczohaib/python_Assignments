def AcceptData():
    return int(input("Enter the Number to Print Star : "));

def PrintPatternInRecursion(size):
    if size != 0:
        size = (size - 1);
        print("*",end=" ")
        PrintPatternInRecursion(size);

def main():
    size = AcceptData();
    PrintPatternInRecursion(size);

if __name__ =="__main__":
    main();