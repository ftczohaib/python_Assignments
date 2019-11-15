class Arithmetic:
    def __init__(self):
        self.value1 = 0;
        self.value2 = 0;

    def Accept(self):
        self.value1 = int(input("Enter the 1st Value : "));
        self.value2 = int(input("Enter the 2nd Value : "));

    def Display(self):
        print ("Entered Value1 is: ",self.value1," and Value2 is: ",self.value2);

    def Addition(self):
        return self.value1 + self.value2;

    def Subtraction(self):
        return self.value1-self.value2;

    def Multiplication(self):
        return self.value1*self.value2;

    def Division(self):
        return self.value1/self.value2;

def main():
    obj1 = Arithmetic();
    obj1.Accept();
    obj1.Display();
    print("Addition : ",obj1.Addition());
    print("Subtraction : ",obj1.Subtraction());
    print("Multiplication : ",obj1.Multiplication());
    print("Division : ",obj1.Division());

    obj2 = Arithmetic();
    obj2.Accept();
    obj2.Display();
    print("Addition : ", obj2.Addition());
    print("Subtraction : ", obj2.Subtraction());
    print("Multiplication : ", obj2.Multiplication());
    print("Division : ", obj2.Division());

if __name__ == "__main__":
    main();
