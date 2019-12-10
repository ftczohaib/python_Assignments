import threading
import re

def ChkSamll(string,lock):
    print(threading.current_thread())
    lock.acquire()
    reg = re.compile("[a-z]")
    for i in string:
        if reg.findall(i):
            print("Small: ",i)
    lock.release()

def ChkCapital(string,lock):
    lock.acquire()
    print(threading.current_thread())
    reg = re.compile("[A-Z]")
    for i in string:
        if reg.findall(i):
            print("Capital: ",i)
    lock.release()

def ChkDigit(string,lock):
    print(threading.current_thread())
    lock.acquire()
    reg = re.compile('[0-9]')
    for i in string:
        if reg.findall(i):
            print("Digi: ",i)
    lock.release()

def main():
    lock = threading.Lock()
    string="Zohaib145148DARUwaLa"
    small = threading.Thread(target=ChkSamll,args=(string,lock))
    capital = threading.Thread(target=ChkCapital,args=(string,lock))
    digit = threading.Thread(target=ChkDigit,args=(string,lock))

    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()

if __name__ == "__main__":
    main()
