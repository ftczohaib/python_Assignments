def AcceptData():
    size = int(input("Enter The Number of Elements to Accept: "));
    arr = list();
    print("Enter the Numbers: ")
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        arr.append(int(input()));
    return arr;

def GetMinimum(arr):
    min = arr[0];
    for i in range(1,len(arr),1):
        if(min > arr[i]):
            min = arr[i];
    return min;

def main():
    listData = AcceptData();
    print("Entered Data is: ",listData);
    print("Maximum Number of Entered Data is : ",GetMinimum(listData));

if __name__ == "__main__":
    main();