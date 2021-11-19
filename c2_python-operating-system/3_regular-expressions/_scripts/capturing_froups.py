import re
res = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")

#print(res)
#<re.Match object; span=(0, 13), match='Lovelace, Ada'>

#print(res.group())
#Lovelace, Ada
#type tuple

#print(res[0])
#Lovelace, Ada
#print(res[1])
#Lovelace
#print(res[2])
#Ada

#print("{} {}".format(res[1],res[2]))
#Lovelace Ada

def rearrange_name(name):
    res = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if res is None:
        return print(name)
    return print("{} {}".format(res[2],res[1]))
#rearrange_name("Ruslan, Liasian")
#rearrange_name("Ruslan, Liasian S.")

#print(re.search(r"[a-zA-Z]{5}", "the weather is sunshime"))
#<re.Match object; span=(4, 9), match='weath'>

#print(re.findall(r"[a-zA-Z]{5}", "the weather is sunshime"))
#['weath', 'sunsh']

#\b matchess word limits
#print(re.findall(r"\b[a-zA-Z]{5}\b", "the weather is sunshime, throu or throuh"))
#['throu']

#print(re.findall(r"\w{5,10}", "the weather is sunshime, throu or throuh looooooooooooong string"))
#['weather', 'sunshime', 'throu', 'throuh', 'looooooooo', 'oooong', 'string']

#print(re.findall(r"\w{5,}", "the weather is sunshime, throu or throuh looooooooooooong stri"))
#['weather', 'sunshime', 'throu', 'throuh', 'looooooooooooong']

#{,1} from zero to up amount of repetitions 2+1=3
#print(re.findall(r"z\w{,2}", "z zz zzz zzzz zzzzz zzzzzz"))
#['z', 'zz', 'zzz', 'zzz', 'z', 'zzz', 'zz', 'zzz', 'zzz']

#{,4} from zero to up amount of repetitions 4+1=5
#rint(re.findall(r"z\w{,4}", "z zz zzz zzzz zzzzz zzzzzz"))
#['z', 'zz', 'zzz', 'zzzz', 'zzzzz', 'zzzzz', 'z']

#The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function
def long_words(text):
  pattern = "[\w]{7,}"
  result = re.findall(pattern, text)
  return result

#print(long_words("I like to drink coffee in the morning.")) # ['morning']
#print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
#print(long_words("I never drink tea late at night."))

log = "it was in september [cage] when i decided to leave the job"
regex = "\[(\d+)\]"
result = re.findall(regex, log)
#print(result)
#print('re.findall result[0] ',result[0])
result = re.search(regex, log)
#print('re.search result[1]',result[1])

def extract_pid_a(log_line):
    regex = "\[(\d+)\]"
    result = re.search(regex, log)
    if result is None:
        return ""
    return result[1]
#print(extract_pid_a(log))

def extract_pid_b(log_line):
    regex = r"\[(\d+)\].*\s([A-Z]+)\s"
    result = re.search(regex, log_line)
    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])
    #(\d+)      -result[1]
    #([A-Z]+)   -result[2]

#print(extract_pid_b("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
#print(extract_pid_b("99 elephants in a [cage]")) # None
#print(extract_pid_b("A string that also has numbers [34567] but no uppercase message")) # None
#print(extract_pid_b("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)

a = re.split(r"[!?.]", "First sentence. Second one? Another one")
#print(a)
#['First sentence', ' Second one', ' Another one']

a = re.split(r"([!?.])", "First sentence. Second one? Another one")
#print(a)
#['First sentence', '.', ' Second one', '?', ' Another one']

x = re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]","Redecived an email from ruslanshamsnet@gmail.com")
#print(x)
#Redecived an email from [REDACTED]

x = re.sub(r"([\w]*)   ([\w]*)", r"\2 \1","Ruslan   Shamsiev")
#print(x)
#Shamsiev Ruslan

x = re.split(r"the|a", "One sentence. Another one? And the last one!")
print(x)
