def AcceptData():
    return int(input("Enter the Number to Print : "));
addition = 0;
def SummationDigit(digit):
    global addition;
    if digit != 0:
        addition = addition + (int(digit % 10));
        digit = int(digit / 10);
        SummationDigit(digit);
    return addition

def main():
    digit = AcceptData();
    print(SummationDigit(digit));

if __name__ =="__main__":
    main();