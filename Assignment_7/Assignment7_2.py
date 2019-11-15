class BankAccount:
    ROI = 10.5;

    def __init__(self):
        self.Name = input("Enter The Name: ");
        self.Amount = float(input("Enter The Amount: "));

    def Deposit(self):
        self.Amount = self.Amount + int(input("Enter The amount To be Deposit: "));

    def Withdraw(self):
        self.Amount = self.Amount - int(input("Enter The amount To be Withdrawn: "));

    def CalculateIntrest(self):
        self.Amount = self.Amount + (self.Amount * self.ROI * 1) / 100;

    def Display(self):
        print ("Account Holder Name : ", self.Name, " and Total Saving: ", self.Amount);


def main():
    obj1 = BankAccount();
    obj1.Display();
    obj1.Deposit();
    obj1.Display();
    obj1.Withdraw();
    obj1.Display();
    print("Before Calculating Interest: ");
    obj1.Display();
    obj1.CalculateIntrest();
    print("After Calculating Interest: ");
    obj1.Display();


if __name__ == "__main__":
    main();
