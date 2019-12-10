import threading
import array

def AddEvenFactor(value):
    evenArr = array.array('i',[]);
    addEven = 0
    for i in range(1,int(value/2)+1,1):
        #print("even: ",i)
        if value % i == 0:
            if i % 2 == 0:
                evenArr.append(i)
                addEven += i
    print(value,"'s Even Factors are :",evenArr," and Addition is: ",addEven)


def AddOddFactor(value):
    oddArr = array.array('i',[])
    addOdd = 0
    for i in range(1,int(value/2)+1,1):
        if value % i == 0:
            if i % 2 != 0:
                oddArr.append(i)
                addOdd += i
    print(value, "'s Odd Factors are :", oddArr, " and Addition is: ", addOdd)


def main():
    evenFactor = threading.Thread(target=AddEvenFactor,args=(36,))
    oddFactor = threading.Thread(target=AddOddFactor,args=(36,))

    evenFactor.start()
    oddFactor.start()

    evenFactor.join()
    oddFactor.join()

    print("Exit From Main")

if __name__ == "__main__":
    main()