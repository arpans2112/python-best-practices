import os
from utilities import projectProperties as pp
from utilities import dateTimeUtils as dtu

root = pp.project_root_path
unique_file_name = dtu.getnowdatetimestf() + ".txt"
file_location = root + "/resources/textFiles/" + unique_file_name

f = open(file_location ,'w')


# operating system module is used to delete the file
"""
os.remove(file_location)
"""

# to check if file exist
if os.path.exists(file_location):
    os.remove(file_location)
    print("we have removed the file", file_location)
else:
    print("The file does not exist")

# Delete entire folder
"""
import os
os.rmdir("myfolder")
"""
