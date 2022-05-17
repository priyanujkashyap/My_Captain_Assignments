Extns= {"py":"Python","c":"C","cpp":"C++","jar":"Java"}
filename = input("Input the Filename: ")
f_extns = filename.split(".")
if f_extns[1] in Extns.keys():
    print("The extention of the file is:", Extns.get(f_extns[1]))
else:
    print("No data available")


