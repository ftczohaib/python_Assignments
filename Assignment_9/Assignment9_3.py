
def CopyFile(fileName):
    fo = open(fileName,'r')
    fw = open("demo.txt",'w')
    fw.write(fo.read())
    fw.close()
    fo = open("demo.txt", 'r')
    print("Data of Copied File: ",fo.read())

    fo.close()
    fo.close()

def main():
    fileName = input("Enter file Name: ")
    CopyFile(fileName)
if __name__ == "__main__":
    main()