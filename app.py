from flask import Flask, request, jsonify, render_template
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as rsa_padding
from cryptography.hazmat.primitives import padding as sym_padding
import os

app = Flask(__name__)

# Example RSA keys (for demonstration purposes)
# In practice, these would be loaded securely or generated securely
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Generate a random AES key
def generate_aes_key():
    return os.urandom(32)  # 32 bytes for AES-256

# Define the encryption and decryption functions
def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            ciphertext += char
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            plaintext += char
    return plaintext

def aes_encrypt(plaintext, key):
    key = key.encode('utf-8')  # Convert to bytes if necessary
    key = key[:32]  # Ensure key is maximum 32 bytes long for AES-256
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\00' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = sym_padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext.hex()

def aes_decrypt(ciphertext, key):
    key = key.encode('utf-8')  # Convert to bytes if necessary
    key = key[:32]  # Ensure key is maximum 32 bytes long for AES-256
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\00' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(bytes.fromhex(ciphertext)) + decryptor.finalize()
    unpadder = sym_padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_data) + unpadder.finalize()
    return plaintext.decode('utf-8')

def rsa_encrypt(plaintext, public_key):
    ciphertext = public_key.encrypt(
        plaintext.encode(),
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext.hex()

def rsa_decrypt(ciphertext, private_key):
    plaintext = private_key.decrypt(
        bytes.fromhex(ciphertext),
        rsa_padding.OAEP(
            mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form.get('text')
    method = request.form.get('method')
    result = ""
    if method == 'caesar':
        shift = int(request.form.get('shift', 3))
        result = caesar_encrypt(plaintext, shift)
    elif method == 'aes':
        key = request.form.get('key')
        result = aes_encrypt(plaintext, key)
    elif method == 'rsa':
        result = rsa_encrypt(plaintext, public_key)
    return jsonify(result=result)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.form.get('text')
    method = request.form.get('method')
    result = ""
    if method == 'caesar':
        shift = int(request.form.get('shift', 3))
        result = caesar_decrypt(ciphertext, shift)
    elif method == 'aes':
        key = request.form.get('key')
        result = aes_decrypt(ciphertext, key)
    elif method == 'rsa':
        result = rsa_decrypt(ciphertext, private_key)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

