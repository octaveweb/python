# while True:
#     try:
#         a = int(input("Enter number 1: ")) 
#         b = int(input("Enter number 2: "))

#         print(f"The division is: {a / b}")
#     except ValueError:
#         print("Plz dont proform bad typecasts")
#     except ZeroDivisionError:
#         print("Hay dont divide by 0")
#     except Exception as e:
#         print("Ops! some error arise -", e)


a = int(input("Enter number 1: ")) 
b = int(input("Enter number 2: "))
if b == 0:
    raise ValueError("Please dont divide by 0")
print(f"The division is: {a / b}")

