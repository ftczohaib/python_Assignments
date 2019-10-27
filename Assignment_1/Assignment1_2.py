def ChkNum(no):
    if (no%2 == 0):
        print(no," Is Even!");
    else:
        print(no," Is Odd!");

def main():
    print("Enter The Number: ");
    num = input();
    ChkNum(int(num));

if __name__ == "__main__":
    main();