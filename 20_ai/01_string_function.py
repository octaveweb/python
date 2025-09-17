def convert_to_hyphen(text):
    
    return text.lower().replace(" ", "-")

string = str(input("Enter a String: "))
print(convert_to_hyphen(string))

# This function converts a string to lowercase and replaces spaces with hyphens.
# Example: "Hello World" becomes "hello-world"