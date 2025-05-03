class Solution():
    def __init__(self):
        self.plaintext = input("Enter the text you would like to encrypt:\n")
        self.cipher = input("Enter the cipher keyword you would like to use:\n")

    def encode(self):
        result = []
        cipher = self.cipher
        cipher_len = len(cipher)
        cipher_index = 0

        for char in self.plaintext:
            if char.isalpha():
                shift = ord(cipher[cipher_index % cipher_len].lower()) - ord('a')
                if char.isupper():
                    encoded = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                else:
                    encoded = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                result.append(encoded)
                cipher_index += 1
            else:
                result.append(char)
        return ''.join(result)

    def decode(self):
        result = []
        cipher = self.cipher
        cipher_len = len(cipher)
        cipher_index = 0

        for char in self.plaintext:
            if char.isalpha():
                shift = ord(cipher[cipher_index % cipher_len].lower()) - ord('a')
                if char.isupper():
                    decoded = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                else:
                    decoded = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                result.append(decoded)
                cipher_index += 1
            else:
                result.append(char)
        return ''.join(result)
