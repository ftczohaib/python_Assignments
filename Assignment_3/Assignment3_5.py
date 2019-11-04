from MarvellousNum import *;

def AcceptData():
    size = int(input("Enter The Number of Elements to Accept: "));
    arr = list();
    print("Enter the Numbers: ")
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        arr.append(int(input()));
    return arr;

def AdditionOfPrime(listData):
    sum = 0;
    primeList = list();
    for i in range(0,len(listData),1):
        if(ChkPrime(listData[i])):
            sum = sum + listData[i];
            primeList.append(listData[i]);
    return primeList,sum;

def main():
    listData = AcceptData();
    print("Entered List is: ",listData);
    print("Prime Numbers and Addition of it in List is : ",AdditionOfPrime(listData));

if __name__ == "__main__":
    main();