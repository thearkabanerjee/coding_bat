def not_string(str):
    if (str[0:4] =="not " or str[0:3] =="not"):
        return str
    else:
        return ("not "+ str)
        
a = not_string("not")
print (a)