import time as t
import sys

import Caesar_Cipher
import Hill_Cipher
import Vigenere_Cipher
import One_Time_Pad_Cipher

going = True
while going == True:
  type = input('''  Enter the encryption system you would like to use:
                                  Caesar Cipher - input 1
                                 Vigenere Cipher - input 2
                               One-Time Pad Cipher - input 3
                                   Hill Cipher - input 4 
                           (Or anything else to exit the program)''')
  if type == '1':
    # implement Caesar Cipher
  elif type == '2':
    # implement Vigenere Cipher
  elif type == '3':
    # implement OTP Cipher
  elif type == '4':
    # implement Hill Cipher
  else:
    print("Thank you for using my Encryption program")
    t.sleep(1)
    sys.exit()
