def AcceptData():
    size = int(input("Enter The Number of Elements to Accept: "));
    arr = list();
    print("Enter the Numbers: ")
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        arr.append(int(input()));
    return arr;

def SumList(arr):
    sum = 0;
    for i in range(0,len(arr),1):
        sum = sum + arr[i];
    return sum;
def main():
    listData = AcceptData();
    print("Entered Data is: ",listData);
    print("Addition of Entered Data is : ",SumList(listData));

if __name__ == "__main__":
    main();