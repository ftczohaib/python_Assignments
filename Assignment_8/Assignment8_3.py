import threading

def AddEvenValue(inputList):
    evenArr = list()
    addEven = 0
    for i in inputList:
        if i % 2 == 0:
            evenArr.append(i)
            addEven += i
    print("Even Values Are :",evenArr," and Addition Is: ",addEven)

def AddOddValue(inputList):
    oddArray = list()
    addOdd = 0
    for i in inputList:
        if not(i % 2 == 0):
            oddArray.append(i)
            addOdd += i
    print("Odd Values Are :", oddArray, " and Addition Is: ", addOdd)


def main():
    inputList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    evenlist = threading.Thread(target=AddEvenValue,args=(inputList,))
    oddlist = threading.Thread(target=AddOddValue,args=(inputList,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()
    
if __name__ == "__main__":
    main()