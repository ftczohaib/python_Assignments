from Arithmetic import *;

def main():
    no1 = int(input("Enter the 1st Number:"));
    no2 = int(input("Enter the 2nd Number:"));
    print("Addition of ",no1," and ",no2," is ",Add(no1,no2));
    print("Subtraction of ", no1, " and ", no2, " is ", Sub(no1, no2));
    print("Multiplication of ", no1, " and ", no2, " is ", Mult(no1, no2));
    print("Division of ", no1, " and ", no2, " is ", Div(no1, no2));

if __name__ == "__main__":
    main();