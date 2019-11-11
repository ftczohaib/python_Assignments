def AcceptData():
    return int(input("Enter the Number to Print : "));

def PrintPatternInRecursion(size):
    if size != 0:
        size = (size - 1);
        PrintPatternInRecursion(size);
        print(size+1,end=" ")


def main():
    size = AcceptData();
    PrintPatternInRecursion(size);

if __name__ =="__main__":
    main();