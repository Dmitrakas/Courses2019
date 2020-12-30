import os
import hashlib
cwd = os.getcwd()
list = [f for f in os.listdir(cwd) if os.path.isfile(f)]
for i in range(len(list)):
  fullPath = os.path.join(cwd, list[i])
  file = open(fullPath, 'rb')
  str_encode = file.read()
  crypt = hashlib.sha3_256()
  crypt.update(str_encode)
  hex = crypt.hexdigest()
  print(str(list[i]) + " " + str(hex))