import fileinput
filename = input("enter file name here: ")

# take back up before changes
with fileinput.FileInput(filename, inplace=True, backup='.bak' ) as file:
    for line in file:
        print(line.replace('a','$'),end='') ## replace a with dollar sign

