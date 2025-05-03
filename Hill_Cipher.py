import numpy as np

class MatrixCipher:
    def __init__(self):
        self.key_matrix = self._get_user_matrix()
        self.size = self.key_matrix.shape[0]
        self.inverse_key = self._modular_inverse_matrix()

    def _get_user_matrix(self):
        print("Enter the size of your square matrix (e.g., 2 for 2x2):")
        while True:
            try:
                n = int(input("Size: "))
                break
            except ValueError:
                print("Please enter a valid integer.")

        print("\nEnter your matrix values row by row, separated by spaces.")
        print("Example for 2x2:\n3 3\n2 5\n")

        matrix = []
        for i in range(n):
            while True:
                try:
                    row = list(map(int, input(f"Row {i + 1}: ").split()))
                    if len(row) != n:
                        raise ValueError
                    matrix.append(row)
                    break
                except ValueError:
                    print(f"Enter exactly {n} integers separated by spaces.")
        
        matrix = np.array(matrix) % 26
        det = int(round(np.linalg.det(matrix))) % 26
        if np.gcd(det, 26) != 1:
            raise ValueError(f"The matrix is not invertible modulo 26 (det = {det}). Please restart with a different matrix.")
        return matrix

    def _modular_inverse_matrix(self):
        det = int(round(np.linalg.det(self.key_matrix))) % 26
        det_inv = pow(det, -1, 26)
        adj = np.round(det * np.linalg.inv(self.key_matrix)).astype(int) % 26
        return (det_inv * adj) % 26

    def _text_to_numbers(self, text):
        return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

    def _numbers_to_text(self, numbers):
        return ''.join([chr(n % 26 + ord('A')) for n in numbers])

    def _chunk_text(self, numbers):
        if len(numbers) % self.size != 0:
            numbers += [0] * (self.size - len(numbers) % self.size)  # Padding with 'A' (0)
        return [numbers[i:i+self.size] for i in range(0, len(numbers), self.size)]

    def encrypt(self, plaintext):
        nums = self._text_to_numbers(plaintext)
        chunks = self._chunk_text(nums)
        result = []
        for chunk in chunks:
            vec = np.dot(self.key_matrix, chunk) % 26
            result.extend(vec)
        return self._numbers_to_text(result)

    def decrypt(self, ciphertext):
        nums = self._text_to_numbers(ciphertext)
        chunks = self._chunk_text(nums)
        result = []
        for chunk in chunks:
            vec = np.dot(self.inverse_key, chunk) % 26
            result.extend(vec)
        return self._numbers_to_text(result)
