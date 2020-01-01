
def DisplayFileData(fileName):
    fd = open(fileName,'r')
    print(fd.read())
    fd.close()

def main():
    fileName = input("Enter File Name : ")
    DisplayFileData(fileName)

if __name__ == "__main__":
    main()