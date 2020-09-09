print("File Content ")
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
string=input('Enter a string to replace :  ')
replace=input('Enter a replacement string : ')
print("After Replacement ")
with open('file.txt', 'r+') as f:
    content = f.read()
    f.seek(0)
    f.truncate()
    f.write(content.replace(string, replace))
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)

