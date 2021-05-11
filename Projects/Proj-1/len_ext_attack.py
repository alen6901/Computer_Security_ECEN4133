from pymd5 import md5, padding
from urllib.parse import quote, urlparse
import urllib, sys
import binascii

#url needs qoutes as a string
url = sys.argv[1]
commandLoc = url.index('&') + 1 
command = url[commandLoc:]
tokenLoc = url.index('token=') + 6
end = commandLoc - 1
length = len(command) + 8
token = ''
i = tokenLoc
while(i < end):
    token += url[i]
    i+=1

pad = padding(length*8)
bits = (length + len(pad))*8
h = md5(state=bytes.fromhex(token), count = bits)
x = "&command=UnlockSafes"
h.update(x)
newToken = h.hexdigest() 
url  = ('https://project1.ecen4133.org/alen6901/lengthextension/api?token='+ newToken + "&" + command + quote(pad) + x)
print(url)
