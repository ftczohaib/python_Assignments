import sys
import os
import hashlib

def HashFile(fileName,blocksize=1024):
    fd = open(fileName,'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)

    fd.close()
    return hasher.hexdigest()

def CompareFile(file1,file2):
    if HashFile(file1) ==  HashFile(file2):
        return True
    else:
        return False

def main():
    isSame = CompareFile(sys.argv[1],sys.argv[2])
    if isSame:
        print("File Data is Same")
    else:
        print("File Data is Not Same")

if __name__ == "__main__":
    main()
