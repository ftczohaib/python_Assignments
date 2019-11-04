def AcceptData():
    size = int(input("Enter The Number of Elements to Accept: "));
    arr = list();
    print("Enter the Numbers: ")
    for i in range(0,size,1):
        print("Enter the ",i+1," value: ");
        arr.append(int(input()));
    return arr;

def GetSearchNumber():
    return int(input("Enter The value to check Occurance in List: "));

def Search(listData,searchDigit):
    cnt=0;
    for i in range(0,len(listData),1):
        if (listData[i] == searchDigit):
            cnt = cnt + 1;
    return cnt;

def main():
    listData = AcceptData();
    searchDigit = GetSearchNumber();
    print("Entered List is: ",listData);
    print("Element to search in List: ", searchDigit);
    print("Occurance of ",searchDigit," in ",listData," is ",Search(listData,searchDigit));

if __name__ == "__main__":
    main();