def missing_char(str, n):
    finalstring = ""
    for i in range(len(str)):
       if (i != n):
          finalstring += str[i]
    
    return finalstring 
    
a = missing_char("arka",1)
print (a)