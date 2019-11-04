def AcceptData():
    return int(input("Enter The Number to Check its Power of 2 : "));
ptrPower = lambda num : 2 ** num;
def main():
    num = AcceptData();
    print("Entered Numer is: ",num," and its Power of 2 is : ",ptrPower(num));

if __name__ == "__main__":
    main();