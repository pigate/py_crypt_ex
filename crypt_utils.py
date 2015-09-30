import sys

def strxor(a, b):
  if len(a) > len(b):
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
  else:
    return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

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

import re

#given a string, drags ' the ' crib across a
#returns list of tuples containing substring of a and index if substring contains only english chars
def filterBarrelsWithTheCrib(a):
  barrels = dragcrib(a, ' the ')
  barrels_filtered = filter(lambda x: re.search(r'\w\w\w\w\w', x[0]) is not None, barrels)
  return barrels_filtered

#there are some spaces that might coincide.
#xor space with space -> \x00 or matching chars
#so after xoring 2 strings, if find \x00, you definitely know there is a space or matching char there
#returns list with indexes of the nulls
def find_nulls(x):
  res = []
  for i, j in enumerate(x):
    if j == '\x00':
      res.append(i) 
  return res

#given 2 strings encrypted with same pad, and dict
#returns pieces of the key in form of dictionary (index -> key) 
def make_cracks(str_a, str_b, diction):
  if type(diction) is not dict:
    raise ValueError('diction is not a dict')
  str_c = strxor(str_a, str_b)
  cracks = find_nulls(str_c)
  #for each crack, xor space with char at str_a (or str_b). res is part of your key
  for crack in cracks:
    k = strxor(' ', str_a[crack])  
    if crack in diction:
      if diction[crack] != k:
        raise ValueError('conflicting keys')
    else:
      diction[crack] = k
