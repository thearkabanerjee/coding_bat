def string_bits(str):
  returnstring = ""
  for i in range(len(str)):
    if (i % 2 == 0):
      returnstring += str[i]
  return returnstring