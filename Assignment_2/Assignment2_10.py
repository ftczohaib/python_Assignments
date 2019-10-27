def getAddition(no):
    sum=0;
    while(no>0):
        rem = no %10;
        sum = sum +rem;
        no = no//10;
    return sum;
def main():
    no1 = int(input("Enter The Number: "));
    print(abs(no1));
    print("Addition of Digit for ",no1," is ",getAddition(no1)," !");

if __name__ == "__main__":
    main();