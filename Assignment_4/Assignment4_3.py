from functools import *;

def AcceptData():
    size = int(input("Enter the Number of Elements: "));
    listData = list();
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        listData.append(int(input()));
    return listData;

def ChkNum(num):
    if (num >= 70 and num <= 90):
        return True;
    else:
        return False;

def Modify(num):
    return  num + 10;

def CalculateProduct(num1,num2):
    return num1*num2;

def main():
    rawList = AcceptData();
    print("Accepted list Is : ",rawList);
    filterList = list(filter(ChkNum,rawList));
    modifyList = list(map(Modify,filterList));
    product = int(reduce(CalculateProduct,modifyList));
    print ("Filtered List :", filterList);
    print ("Modified List :", modifyList);
    print("Product of Modified List : ",product);

if __name__ == "__main__":
    main();