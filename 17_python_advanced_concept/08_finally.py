def divide(a,b):
    
        try:
            c = a / b
            print(c)
            return c

        except Exception as e:
            print(e)
            return None
        # This will always excuted no matter if try completely excuted or not 
        finally:
            print("This will always excuted!")

a = int(input("Enter number 1: ")) 
b = int(input("Enter number 2: ")) 
divide(a,b)
