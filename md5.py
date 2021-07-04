import hashlib
import sys

# (C) Ujwalkarumuri

def cmd():
    line=str(input("enter the line to convert into string \n : "))
    if (len(line) >= 1):
        return (hashup(line))
    else:
        print("hashing requires non empty input")
        exit(1)

def boxprint(_string):
    element = "-"
    header = (element * len(_string) + "\n")
    footer = ("\n"+element * len(_string) + "\n")
    return(header + _string + footer)

def hashup(_string):
    return (hashlib.md5(_string.encode('utf-8')).hexdigest())

if (len(sys.argv) > 1 ) and type(sys.argv[1] == str):
    if (sys.argv[1] != "--help" ):
        print(boxprint(hashup(sys.argv[1])))
    else:
        print(sys.argv[0]+":"+"converts string to md5")
        print()
        print("Usage:")
        print("python " + sys.argv[0] + " <string>")
else:
    print(boxprint(cmd()))
