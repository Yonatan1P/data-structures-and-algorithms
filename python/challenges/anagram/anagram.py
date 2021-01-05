def check_anagram(string1,string2):
  string1 = string1.lower()
  string1 = string1.replace(' ','')
  string2 = string2.lower()
  string2 = string2.replace(' ','')
  for char in string1:
    if char in string2:
      string1 = string1.replace(f'{char}','')
      string2 = string2.replace(f'{char}','')
  return not string1 and not string2
