class Numbers:
    def __init__(self):
        self.value=int(input("Enter the Value: "));

    def ChkPrime(self):
        isPrime=True;
        for i in range(2,(self.value//2)+1,1):
            if self.value%i == 0:
                isPrime=False;
                break;
        return isPrime;

    def ChkPerfect(self):
        isPerfect=False;
        sum = 0;
        for i in range(1,(self.value//2)+1,1):
            if self.value%i==0:
                sum =sum+i;
        if sum == self.value:
            isPerfect=True;
        return isPerfect;

    def FactorsList(self):
        isFactors = False;
        factorList = list();
        for i in range(1, (self.value // 2) + 1, 1):
            if self.value % i == 0:
                factorList.append(i)
        factorList.append(self.value);
        return factorList;

    def factorSum(self):
        sum=0;
        factorList = self.FactorsList();
        for i in range(0,len(factorList),1):
            sum = sum + factorList[i]
        return sum;

    def Display(self):
        return self.value;

def main():
    obj1=Numbers();
    if(obj1.ChkPrime()):
        print("Number ",obj1.Display()," is Prime;")
    else:
        print("Number ", obj1.Display(), " is not a Prime;")

    if (obj1.ChkPerfect()):
        print("Number ", obj1.Display(), " is Perfect;")
    else:
        print("Number ", obj1.Display(), " is not a Perfect;")

    print("All Factors of ", obj1.Display(), " is ",obj1.FactorsList())
    print("Total of Factors of ", obj1.Display(), " is ", obj1.factorSum())


if __name__ == "__main__":
    main();
