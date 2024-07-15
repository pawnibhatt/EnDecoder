Basic Encryption and Decryption Tool/Web Application
This is a web application that allows users to encrypt and decrypt text using three different encryption methods: Caesar Cipher, AES, and RSA.
Files
•	app.py: The Flask application file that handles encryption and decryption requests.
•	index.html: The HTML file that provides the user interface for the application.
•	ht.js: The JavaScript file that handles form submissions and updates the result field.
•	style.css: The CSS file that styles the application.
How to Use
Running the Application
1.	Open a terminal.
2.	Type python app.py to start the Flask development server.
3.	Open a web browser and navigate to the IP address and port number displayed in the terminal, for example: http://127.0.0.1:5000.
Using the Application
1.	Enter your desired text in the input field.
2.	Choose the encryption or decryption method you want to use: Caesar Cipher, AES, or RSA.
3.	If using Caesar Cypher, directly press “Encode” or “Decode” to perform the function.
4.	If using AES, enter a 32-byte key. You can generate an AES key online using a tool such as AES Key Generator. Or you can use our generated key: 16Xqp1KO6fIGy9ZncjoKzDQLcsTE8pdF
5.	If using RSA, enter a public key or private key. You can generate an RSA key pair using a tool such as OpenSSL. For example, to generate a key pair using OpenSSL, run the following commands:
#  openssl genrsa -out private_key.pem 2048
# openssl rsa -pubout -in private_key.pem -out public_key.pem
Or if you don’t really have a key just type anything for example “email.com” the default key would automatically activate.
6.	Press the "Encrypt" or "Decrypt" button to perform the operation.
7.	The result will be displayed in the result field.
Encryption Methods
Caesar Cipher
The Caesar Cipher is a simple substitution cipher that replaces each letter with a letter a fixed number of positions down the alphabet.
AES
AES (Advanced Encryption Standard) is a symmetric-key block cipher that is widely used for encrypting data at rest and in transit.
RSA
RSA (Rivest-Shamir-Adleman) is an asymmetric-key algorithm that is widely used for encrypting data and creating digital signatures.
Note
This application is for educational purposes only and should not be used for encrypting sensitive data in production. In particular, the RSA key pair generation process is not secure and should not be used in production.

