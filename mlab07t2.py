s = input("Vvedite povidomlennya: ")
n = int(input("Zmist v storonu: "))
encryption = " "
for char in s:
    if char == " ":
        encryption += char
    else: 
        shift = chr(ord(char) + n)
        encryption += shift
print("Result: ", encryption)
