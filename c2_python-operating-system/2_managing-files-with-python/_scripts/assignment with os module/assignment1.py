import os
#1
def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "a") as file:
        file.write(comments)
        #file.close()
    filesize = os.path.getsize(filename)
    return(filesize)

print(create_python_script("program.py"))



#2
def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open ("script.py","w") as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))



#4
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open ("newfile.txt","w") as file:
    pass
  timestamp = os.path.getmtime("newfile.txt")
  # Convert the timestamp into a readable format, then into a string
  x = datetime.datetime.fromtimestamp(timestamp).date()
  #print(x)
  # Return just the date portion
  # Hint: how many characters are in “yyyy-mm-dd”?
  return ("{}".format(x))

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd

#5
def parent_directory():
  # Create a relative path to the parent
  # of the current working directory
  #relative_parent = os.path.join(___, ___)
  relative_parent = os.path.join(os.getcwd(), os.pardir)
  print('os.pardir',os.pardir)
  print('os.getcwd()',os.getcwd())

  # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

print(parent_directory())
