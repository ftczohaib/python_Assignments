import threading

def DisplaySerialize(lock):
    lock.acquire()
    for i in range(1,51,1):
        print("Serialize: ",i)
    lock.release()

def DisplayReverse(lock):
    lock.acquire()
    for i in range(50,0,-1):
        print("Reverse: ",i)
    lock.release()


def main():
    lock = threading.Lock()
    thread1 = threading.Thread(target=DisplaySerialize,args=(lock,))
    thread2 = threading.Thread(target=DisplayReverse,args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

if __name__ == "__main__":
    main()