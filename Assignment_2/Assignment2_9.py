def getLength(no):
    cnt=0;
    while (no > 0):
        rem = no % 10;
        no = no // 10;
        cnt = cnt + 1;
    return cnt;
def main():
    no1 = int(input("Enter The Number: "));
    print(abs(no1));
    print("Number of Digit for ",no1," is ",getLength(no1)," !");

if __name__ == "__main__":
    main();