Project README
Encryption Techniques in Python
This Python script comprises implementations of three encryption techniques: Caesar Cipher, Substitution Cipher, and RSA (Rivest-Shamir-Adleman) encryption. Each method serves a specific purpose and demonstrates fundamental concepts of encryption.

1. Caesar Cipher
Encrypt
The encryptcaesar function allows you to encrypt a message using the classic Caesar Cipher method. The script prompts you to input the message, and it shifts the letters by a fixed amount to provide the encrypted output.

Decrypt
Conversely, the decryptcaesar function decrypts a message encrypted using Caesar Cipher. It asks for the encrypted message and reveals the original message by shifting the letters back.

2. Substitution Cipher
Encrypt
For the Substitution Cipher, the encryptsubstitution function employs a randomly generated key to substitute each character in the input message, providing an encrypted output.

Decrypt
The decryptsubstitution function decrypts the message by reversing the substitution process, requiring the original key for accurate decryption.

3. RSA Encryption
The RSA encryption implementation includes functions for key generation, encryption (encryptrsa), and decryption (decryptrsa). To use RSA, it is essential to have a basic understanding of public and private key pairs, as well as modular arithmetic.

Key Generation
To generate RSA keys, you can use the rsakeysgen function. It prompts you to input prime numbers and then calculates the public and private keys.

Encryption and Decryption
Once the keys are generated, you can utilize the encryptrsa function to encrypt a message and decryptrsa to decrypt it. These functions prompt for the necessary keys and input, providing the encrypted or decrypted output accordingly.

4. Diffie-Hellman Key Exchange
For Diffie-Hellman key exchange, the diffiekeysgen function generates the private and public keys required for secure communication. Understanding the concept of primitive roots is beneficial for effective use.

Note: While efforts have been made to streamline the processes, it is crucial to have a certain level of knowledge about encryption, especially for RSA and Diffie-Hellman. Using this script, a complete beginner may find certain functions complex. If you encounter any challenges, feel free to reach out for assistance.

Usage
To use the encryption functions, you can call them individually, such as encryptcaesar, encryptsubstitution, encryptrsa, etc. Follow the prompts to input the necessary information for encryption or decryption.

Caution: The RSA and Diffie-Hellman functions require careful input and understanding of their respective key generation processes. Users unfamiliar with these concepts may find the encryption and decryption processes less intuitive.