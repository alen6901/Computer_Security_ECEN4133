#!/usr/bin/python3
# coding: latin-1
good = "Use SHA-256 instead!"
evil = "MD5 is perfectly secure!"
blob = """                 �_��[�J�`H'�"Q-���h#�y�m������n��Khn:�O5:y���2�}��"+��)�/8�"P"����7��5"?�|9��[Mo��,�
h��l���2zG�{C�O��$�B���j9"""
from hashlib import sha256
z = sha256((blob).encode("latin-1")).hexdigest()
i = int(z, 16)
if(i%2 == 0):
  print(good)
else:
  print(evil)