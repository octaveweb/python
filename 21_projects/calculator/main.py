

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter first number: "))
    print("Opration\n--------------\nPress + to addition\nPress - subtract\nPress * to multiply\nPress / Divide")

    o = input("Enter Opration: ")

    match o:
        case "+":
            print(f"resule is {a+b}")
        case "-":
            print(f"resule is {a-b}")
        case "*":
            print(f"resule is {a*b}")
        case "/":
            print(f"resule is {a/b}")
        case default:
            print("Some Error Arived!")
except Exception as e:
    print(f"Enter a valid value {e}")