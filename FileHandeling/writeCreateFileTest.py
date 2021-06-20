from utilities import  projectProperties as pp
from utilities import dateTimeUtils as dtu
import datetime
root = pp.project_root_path
unique_file_name = dtu.getnowdatetimestf() + ".txt"
# print(root,unique_file_name)
# append content to the existing file
"""
n_file = open(root + "/resources/textFiles/" + unique_file_name , 'a')
n_file.write("Hi I'm arpan who created this file")
n_file.close()
"""

# over-rite the existing file.
"""
n_file = open(root + "/resources/textFiles/01_17_21_06_18_21.txt", 'w')
n_file.write("Hi I'm arpan who created this file")
n_file.close()
"""

# it will create a file, but it will thow an error if file already exist.
# n_file = open(root + "/resources/textFiles/01_17_21_06_18_21.txt", 'x')
n_file = open(root + "/resources/textFiles/" + unique_file_name, 'x')
n_file.write("Hi I'm arpan who created this file")
n_file.close()








