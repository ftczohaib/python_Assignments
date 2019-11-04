from functools import *;

def AcceptData():
    size = int(input("Enter the Number of Elements: "));
    listData = list();
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        listData.append(int(input()));
    return listData;

def ChkPrime(num):
    isPrime = True;
    for i in range(2,((num//2)+1),1):
        if (num%i == 0):
            isPrime = False;
            break;
    return isPrime;

def Modify(num):
    return  num * 2;

def Maximum(num1,num2):
    if(num1 < num2):
        num1,num2 = num2,num1;
    return num1;

def main():
    rawList = AcceptData();
    print("Accepted list Is : ",rawList);
    filterList = list(filter(ChkPrime,rawList));
    print ("Filtered List :", filterList);
    modifyList = list(map(lambda num : num*2,filterList));
    print ("Modified List :", modifyList);
    max = int(reduce(Maximum,modifyList));
    print("Product of Modified List : ",max);

if __name__ == "__main__":
    main();