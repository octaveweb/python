def dictiotor(func):
    def wrapper():
        print("\n")
        func()
        print("\n")
    return wrapper

def readMode(filename):
    f = open(f"{filename}", "r")
    content = f.read()
    print(content)
    f.close()


def writeMode(filename):

    f = open(f"{filename}", "w")

    string = str(input("Enter a String:"))

    f.write(string)

    f.close()


def appendMode(filename):
    f = open(f"{filename}", "a")

    string = str(input(f"Write text to add into {filename}:"))

    f.write(string)

    f.close()

    

def file(filename, mode):
    match mode:
        case "1":
            print("\n")
            print("Read Mode Active:")
            readMode(filename)
            print("\n")
        case "2":
            print("\n")
            print("Write Mode Active:")
            writeMode(filename)
            print("\n")
        case "3":
            print("\n")
            print("Append Mode Active:")
            appendMode(filename)
            print("\n")
        

            
            

filename = input("Enter name od file: ")
mode = input("Mode\n1 = read mode\n2 = write mode\n3 = append mode\nEnter mode of file: ")
file(filename, mode)
