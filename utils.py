import sys

def strxor(a, b):
  if len(a) > len(b):
    return "".join([chr[ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr[ord(x) ^ or(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
  return open("/dev/urandom").read(size)

#drags crib across a. 
#returns array of tuples of cribbed word in a with index it starts on
def dragcrib(a, crib):
  if (len(crib) > len(a)):
    return (strxor(crib, a), 0)
  #for every sub = substring(len(b)) of a,  
  # xored = xor(crib, sub)
  # add to list, (xored, index)
  i = 0
  j = i + len(crib)
  res = []
  while j < len(a):
    sub = a[i:j]
    xored = strxor(crib, sub)
    i = i + 1 
    j = i + len(crib)
    res.append((xored, i))
  return res

//there are some spaces that might coincide.
//xor space with space -> \x00
//so after xoring 2 strings, if find \x00, you definitely know there is a space there
//returns list with indexes of the spaces
def find_spaces(x):
  res = []
  for i, j in enumerate(x):
    if j == '\x00':
      res.append(i) 
  return res
