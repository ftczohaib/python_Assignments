def AcceptData():
    return int(input("Enter the Number to Print : "));
fact = 1;
def GetFactorial(digit):
    global fact;
    if digit > 0:
        fact = fact * digit;
        digit = digit - 1
        GetFactorial(digit);
    return fact

def main():
    digit = AcceptData();
    print(GetFactorial(digit));

if __name__ =="__main__":
    main();