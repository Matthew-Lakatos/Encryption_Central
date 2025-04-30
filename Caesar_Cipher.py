# Caesar Cipher code class
class Solution():
  self.char_map = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
  def __init__(self):
    self.plaintext = input("Enter the text you would like to encrypt:\n")
    self.shift_chars = int(input("Enter the number of places you would like to shift each character by by:\n")) % 26
    try:
      self.shift_pos = int(input("Enter the number of places you would like to shift each character's position by:\n")) % len(self.plaintext)
    except:
      self.shift_pos = 0
  def encode(self):
    ciphertext_nonshift = ""
      try: 
        ciphertext_nonshift += str(char_map.find(self.char_map[element] + self.shift_pos))
      except:
        ciphertext_nonshift += str(element)
    print(ciphertext_nonshift)
    ciphertext = [0] * len(ciphertext_nonshift)
    for i in xrange(len(ciphertext_nonshift)):
      ciphertext[- i - self.shift_pos] = ciphertext_nonshift[i]
    print(ciphertext)
    print(''.join(ciphertext))
    return ''.join(ciphertext)
    
