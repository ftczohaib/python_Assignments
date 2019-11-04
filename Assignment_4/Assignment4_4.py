from functools import *;

def AcceptData():
    size = int(input("Enter the Number of Elements: "));
    listData = list();
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        listData.append(int(input()));
    return listData;

def ChkEven(num):
    if (num%2 == 0):
        return True;
    else:
        return False;

def Modify(num):
    return  num * num;

def CalculateSum(num1,num2):
    return num1+num2;

def main():
    rawList = AcceptData();
    print("Accepted list Is : ",rawList);
    filterList = list(filter(ChkEven,rawList));
    modifyList = list(map(Modify,filterList));
    sum = int(reduce(CalculateSum,modifyList));
    print ("Filtered List :", filterList);
    print ("Modified List :", modifyList);
    print("Product of Modified List : ",sum);

if __name__ == "__main__":
    main();