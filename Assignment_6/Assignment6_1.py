class Demo:
    value =0;
    def __init__(self):
        self.no1 = int(input("Enter 1st Number: "));
        self.no2 = int(input("Enter 2nd Number: "));

    def fun(self):
        print("Entered Number by User is",self.no1," and ",self.no2);

    def gun(self):
        print("Entered Number by User is",self.no1," and ",self.no2);

def main():
    obj1 = Demo();
    obj2 = Demo();
    obj1.fun();
    obj2.fun();
    obj1.gun();
    obj2.gun();

if __name__ == "__main__":
    main()