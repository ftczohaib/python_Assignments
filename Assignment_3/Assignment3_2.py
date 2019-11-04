def AcceptData():
    size = int(input("Enter The Number of Elements to Accept: "));
    arr = list();
    print("Enter the Numbers: ")
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        arr.append(int(input()));
    return arr;

def GetMaximum(arr):
    max = arr[0];
    for i in range(1,len(arr),1):
        if(max < arr[i]):
            max = arr[i];
    return max;

def main():
    listData = AcceptData();
    print("Entered Data is: ",listData);
    print("Maximum Number of Entered Data is : ",GetMaximum(listData));

if __name__ == "__main__":
    main();