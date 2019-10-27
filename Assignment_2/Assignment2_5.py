def isPrime(no1):
    primeFlag = True;
    for i in range(2,(no1//2)+1):
        if no1%i == 0:
            primeFlag = False;
        break;
    return  primeFlag;
def main():
    no1 = int(input("Enter The Number:"));
    if isPrime(no1):
        print("Entered Value ",no1," is a Prime Number !");
    else:
        print("Entered Value ", no1, " is not a Prime Number !");

if __name__ == "__main__":
    main();