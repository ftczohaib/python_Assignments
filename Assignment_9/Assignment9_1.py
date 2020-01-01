def ChkFile(fileName):
    try:
        fo = open(fileName,'r')
        return True
    except:
        return False


def main():
    fileName = input("Enter File Name to Check: ");
    chkFile = ChkFile(fileName)
    if chkFile:
        print("File is Present!")
    else:
        print("File is Not Present!")

if __name__ == "__main__":
    main()





