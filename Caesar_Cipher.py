# Caesar Cipher code class
class Solution:
    def __init__(self):
        self.plaintext = input("Enter the text you would like to encrypt:\n")
        self.shift_chars = int(input("Enter the number of places you would like to shift each character by:\n")) % 26
        try:
            self.shift_pos = int(input("Enter the number of places you would like to shift each character's position by:\n")) % len(self.plaintext)
        except:
            self.shift_pos = 0

    def encode(self):
        ciphertext_nonshift = ""

        for char in self.plaintext:
            if char.isalpha():
                if char.isupper():
                    base = ord('A')
                else:
                    base = ord('a')
                shifted = (ord(char) - base + self.shift_chars) % 26
                ciphertext_nonshift += chr(base + shifted)
            else:
                ciphertext_nonshift += char

        # Shift positions of characters
        ciphertext = [''] * len(ciphertext_nonshift)
        for i in range(len(ciphertext_nonshift)):
            new_index = (i + self.shift_pos) % len(ciphertext_nonshift)
            ciphertext[new_index] = ciphertext_nonshift[i]

        encrypted = ''.join(ciphertext)
        print("Encrypted text:", encrypted)
        return encrypted
      
    def decode(self, ciphertext):
        # Step 1: Undo position shift (rotate in the opposite direction)
        n = len(ciphertext)
        shifted_back = [''] * n
        for i in range(n):
            original_index = (i - self.shift_pos) % n
            shifted_back[original_index] = ciphertext[i]
        unshifted_text = ''.join(shifted_back)

        # Step 2: Undo Caesar character shift
        decrypted = ""
        for char in unshifted_text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - base - self.shift_chars) % 26
                decrypted += chr(base + shifted)
            else:
                decrypted += char

        print("Decrypted text:", decrypted)
        return decrypted
