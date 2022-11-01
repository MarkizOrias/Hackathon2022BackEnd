# Python program to find the SHA-1 message digest of a file

# importing the hashlib module
import hashlib

user_input = r"file directory"


def hash_file(filename):
   """"This function returns the SHA-256 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha256()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest

   return h.hexdigest()

message = hash_file(user_input)
print(message)
