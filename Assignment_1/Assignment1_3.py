def add(x,y):
    return x+y;

def main():
    print("Enter 1st Number:");
    x=input();
    print("Enter 2nd Number:");
    y = input();
    z = add(int(x),int(y));
    print("Addition of : ",x," and ",y," is ",z);

if(__name__ == "__main__"):
    main();