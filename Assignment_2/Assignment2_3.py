def Factorial(no1):
    fact = no1;
    for i in range(no1,1,-1):
        fact = fact * (i-1);
    return  fact;
def main():
    no1 = int(input("Enter The Number:"));
    print("Factorial of ",no1," is ",Factorial(no1),"!");

if __name__ == "__main__":
    main();