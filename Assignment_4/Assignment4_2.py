def AcceptData():
    return int(input("Enter The 1st Number : ")),int(input("Enter The 2nd Number: "));
ptrPower = lambda num1,num2 : num1*num2;
def main():
    num1,num2 = AcceptData();
    print("Entered 1st Number is: ",num1," and Entered 2nd Number is: ",num2," and both Multipication is : ",ptrPower(num1,num2));

if __name__ == "__main__":
    main();