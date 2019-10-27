def checkDivisible(num):
    if(num%5 == 0):
        return True;
    else:
        return False;
def main():
    print("Enter the Number: ");
    x=int(input());
    print(checkDivisible(x));
if(__name__ == "__main__"):
    main();