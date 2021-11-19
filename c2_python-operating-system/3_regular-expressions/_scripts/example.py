#https://regex101.com/
import re

#grep word /usr/share/dict/word

#regardless of uppercase or lowercase
#grep -i word /usr/share/dict/word

#for searching all possible variants a 'dot' or . matches all the characters for instance:
# wosd
# wokd
# woNd
#grep wo.d /usr/share/dict/word

#for searching all possible variants which starts with ^ should be addded . matches all the characters for instance:
# wosd...
# wokd...
# woNd...
#grep ^wo.d /usr/share/dict/word

#for searching all possible variants which ends with $ should be addded . matches all the characters for instance:
# woodwind
# word
# upward
#grep w..d& /usr/share/dict/word

result = re.search(r"aza", "plaza")#rawstring
#print(result)
#<re.Match object; span=(2, 5), match='aza'>
result = re.search(r"aza", "bazar")#rawstring
#print(result)
#<re.Match object; span=(1, 4), match='aza'>
result = re.search(r"aza", "ffr")#rawstring
#print(result)
#None
result = re.search(r"^s", "ssuper")#rawstring
#print(result)
#<re.Match object; span=(0, 1), match='s'>
result = re.search(r"..l.x", "relaxGN")#rawstring
#print(result)
#<re.Match object; span=(0, 5), match='relax'>
result = re.search(r"..l.x", "relaxGN")#rawstring
#print(result)
#<re.Match object; span=(0, 5), match='relax'>
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

#print(check_aei("academia")) # True
#print(check_aei("aerial")) # False
#print(check_aei("paramedic")) # True

#print(re.search(r"isk", "AsterIsK",re.IGNORECASE))
#<re.Match object; span=(5, 8), match='IsK'>

#print(re.search(r"[Ss]SH", "SSH"))
#<re.Match object; span=(0, 3), match='SSH'>


#print(re.search(r"[a-z]ocket", "sasfasfsocket"))
#<re.Match object; span=(7, 13), match='socket'>

#print(re.search(r"[a-zA-Z0-9]athe...ics", "123490mathematics"))
#<re.Match object; span=(6, 17), match='mathematics'>

#print(re.search(r"[a-zA-Z0-9]*athe...ics", "123490mathematics"))
#<re.Match object; span=(0, 17), match='mathematics'>

def check_punctuation (text):
  result = re.search(r"[\,\.\:\;\?\!]", text)
  #result = re.search(r"[^a-zA-Z]", text)
  return result != None

#print(check_punctuation("This is a sentence that ends with a period.")) # True
#print(check_punctuation("This is a sentence fragment without a period")) # False
#print(check_punctuation("Aren't regular expressions awesome?")) # True
#print(check_punctuation("Wow! We're really picking up some steam now!")) # True
#print(check_punctuation("End of the line")) # False

#print(re.search(r"[^a-zA-Z]", "Thisis a sentence that ends with a period."))
#<re.Match object; span=(6, 7), match=' '>

#print(re.search(r"pen|cars", "I have a lot of pencils"))
#<re.Match object; span=(16, 19), match='pen'>

#print(re.search(r"pen|cars", "I have a lot of pencils and cars"))
#<re.Match object; span=(16, 19), match='pen'>

#print(re.findall(r"p.n|ca.s", "I have a lot of pencils and cars"))
#['pen', 'cars']

#print(re.findall(r"p.*e|w.k", "I need more practice at this moment to find a work"))
#['practice at this mome']

#print(re.search(r"p.*thon", "I need some more practice on python at this moment to find a work"))
#<re.Match object; span=(17, 35), match='practice on python'>

#print(re.search(r"p[a-z]*n", "I need some more practice on python at this moment to find a work"))
#<re.Match object; span=(29, 35), match='python'>

#print(re.search(r"r+V+", "rVsgasgasga"))
#<re.Match object; span=(0, 2), match='rV'>

#print(re.search(r"r+V+", "rrrrVvVV"))
#<re.Match object; span=(0, 5), match='rrrrV'>

def repeating_letter_a(text):
  result = re.search(r"[aA].*[aA]", text)
  return result != None

#print(repeating_letter_a("banana")) # True
#print(repeating_letter_a("pineapple")) # False
#print(repeating_letter_a("Animal Kingdom")) # True
#print(repeating_letter_a("A is for apple")) # True

#print(re.search(r"x?lly", "really loooong really string"))
#<re.Match object; span=(3, 6), match='lly'>

#print(re.search(r"rea?lly", "really loooong really"))
#<re.Match object; span=(0, 6), match='really'>

#print(re.search(r"\.com", "www.google.com"))
#<re.Match object; span=(10, 14), match='.com'>

#print(re.search(r"\w*", "www.google.com"))
#<re.Match object; span=(0, 3), match='www'>

#print(re.search(r"\w*", "some_a_web_site123123"))
#<re.Match object; span=(0, 21), match='some_a_web_site123123'>

#print(re.search(r"\d+", "some_a_web_site123123"))
#<re.Match object; span=(15, 21), match='123123'>

#print(re.findall(r"\s", "some a web site123123"))#whitespace characters
#[' ', ' ', ' ']

#print(re.findall(r"\b", "word1"))#whitespace characters
#['', '']

#print(re.findall(r"\b", "word1 word2"))#whitespace characters
#['', '', '', '']

def check_character_groups(text):
  result = re.search(r"\w +", text)
  return result != None

#print(check_character_groups("One")) # False
#print(check_character_groups("123  Ready Set GO")) # True
#print(check_character_groups("username user_01")) # True
#print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

#print(re.findall(r"[a-z]{2,}", "word1 asfasfasa 35252352 vdsvsdvsdv x sm"))
#['word', 'asfasfasa', 'vdsvsdvsdv', 'sm']

#print(re.search(r"T.*a", "Texas"))
#<re.Match object; span=(0, 4), match='Texa'>

#print(re.search(r"^T.*a$", "Texas"))
#None

#print(re.search(r"^t.*s$", "Texas again", re.IGNORECASE))
#None

#print(re.search(r"^t.*s$", "Texas", re.IGNORECASE))
#<re.Match object; span=(0, 5), match='Texas'>

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
#print(re.search(pattern, "new_strSng"))
#<re.Match object; span=(0, 10), match='new_strSng'>

#print(re.search(pattern, "new string"))
#None

#print(re.search(pattern, "new_12312string"))
#<re.Match object; span=(0, 15), match='new_12312string'>

#print(re.search(pattern, "1new_string"))
#None

def check_sentence(text):
  #print(re.findall(r"^[A-Z][a-z ]*[\.\?\!]$", text))
  #return result != None
  pass

check_sentence("Is this is a sentence?") # True
check_sentence("is this is a sentence?") # False
check_sentence("Hello") # False
check_sentence("1-2-3-GO!") # False
check_sentence("A star is born.") # True

s = '<html><head><title>Title</title>'
#print(re.match('<.*?>', s))
#<re.Match object; span=(0, 6), match='<html>'>

#print(re.match('<.*>', s))
#<re.Match object; span=(0, 32), match='<html><head><title>Title</title>'>
