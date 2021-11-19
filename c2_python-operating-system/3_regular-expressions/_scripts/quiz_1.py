import re
#1
def check_web_address(text):
  pattern = "^[\w\.\-\+]+[come|info|edu]*$"
  result = re.findall(pattern, text)
  #print(result)

check_web_address("gmail.com") # True
check_web_address("www@google") # False
check_web_address("www.Coursera.org") # True
check_web_address("web-address.com/homepage") # False
check_web_address("My_Favorite-Blog.US") # True


#2
def check_time(text):
  pattern = "^([1-9]|[012])+\:[0-5]+[0-9]+[ ]*[aApPmM]+$"
  result = re.search(pattern, text)
  #print(result)

check_time("12:45pm") # True
check_time("9:59 AM") # True
check_time("6:60am") # False
check_time("five o'clock") # False


#3
def contains_acronym(text):
  pattern = "[\(][a-z(A-Z)+0-9]{2,}[\)]"
  result = re.search(pattern, text)
  #print(result)

contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication") # True
contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication") # True
contains_acronym("Please do NOT enter without permission!") # False
contains_acronym("PostScript is a fourth-generation programming language (4GL)") # True
contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!") # True



#5
def check_zip_code (text):
  result = re.search(r"([^\d])[\s][\d]{5}([\-])*(([\d]){4})*", text)
  #print(result)

check_zip_code("The zip codes for New York are 10001 thru 11104.") # True
check_zip_code("90210 is a TV show") # False
check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.") # True
check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.") # False
