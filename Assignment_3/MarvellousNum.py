def ChkPrime(num):
    isPrime = True;
    for i in range(2,((num//2)+1),1):
         if(num%i == 0):
            isPrime =  False;
    return isPrime

