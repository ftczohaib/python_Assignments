def getLength(no):
    return len(str(abs(no)));
def main():
    no1 = int(input("Enter The Number: "));
    print(abs(no1));
    print("Number of Digit for ",no1," is ",getLength(no1)," !");

if __name__ == "__main__":
    main();