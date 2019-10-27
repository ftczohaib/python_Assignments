def printPattern(num):
    for i in range(0,num):
        print("* ",end="");
def main():
    print("Enter the Number: ");
    x=int(input());
    printPattern(x);
if(__name__ == "__main__"):
    main();