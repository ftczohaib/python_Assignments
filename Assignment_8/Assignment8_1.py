import threading

def DisplayEven(value):
    counter = 0
    for i in range(1,value,1):
        if counter <= 10:
            if i % 2 == 0:
                print("Even: ",i)
                counter += 1
        else:
            return

def DisplayOdd(value):
    counter=0
    for i in range(1,value,1):
        if counter <= 10:
            if i % 2 != 0:
                print ("Odd: ",i)
                counter += 1
        else:
            return


def main():
    even = threading.Thread(target=DisplayEven,args=(30,))
    odd = threading.Thread(target=DisplayOdd,args=(30,))

    even.start()
    odd.start()

    even.join()
    odd.join()

if __name__ == "__main__":
    main()
