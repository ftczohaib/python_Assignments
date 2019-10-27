def checkLength(str):
    return len(str);

def main():
    value = input("Enter The Name:");
    print("Entered Value ",value,"'s length is ",checkLength(value));

if(__name__ == "__main__"):
    main();