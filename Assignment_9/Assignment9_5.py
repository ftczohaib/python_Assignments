import sys

def FindInFile(fileName,toSearch):
    fo = open(fileName,'r')
    cnt = 0
    for line in fo:
        if toSearch in line:
            cnt = cnt +1
    return cnt

def main():
    cnt = FindInFile(sys.argv[1],sys.argv[2])
    print("Occurance of string in File : ",cnt)

if __name__ == "__main__":
    main()