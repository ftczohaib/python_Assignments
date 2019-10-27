def checkValue(value):
    if(value < 0):
        print("Entered Number ",value," is Negative!");
    elif(value > 0):
        print("Entered Number ",value," is Positive!");
    else:
        print("Entered Number ",value," Is Zero!");

def main():
    print("Enter the Number: ");
    no = int(input());
    checkValue(no);
if(__name__=="__main__"):
    main();