#!/usr/bin/python3
# coding: latin-1
good = "Use SHA-256 instead!"
evil = "MD5 is perfectly secure!"
blob = """                 2O��.�X-�i�h�o������iQ]�y�l:��y�����G�����C�xlۉD�-�R&�NOƅ#8@J�:��5��D��*������`}�Oq�i6����ѯ��s��R~�R��Z������"""
from hashlib import sha256
z = sha256(blob).hexdigest()
i = int(z, 16)
if(i%2 == 0):
  print(good)
else:
  print(evil)