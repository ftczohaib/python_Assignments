def Factors(no1):
    fact = 0;
    for i in range(1,(no1//2)+1):
        if no1%i == 0:
            fact = fact + i;
    return  fact;
def main():
    no1 = int(input("Enter The Number:"));
    print("Addition of ",no1," Factor is ",Factors(no1),"!");

if __name__ == "__main__":
    main();