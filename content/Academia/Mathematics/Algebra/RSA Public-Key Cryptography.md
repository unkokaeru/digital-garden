# RSA Public-Key Cryptography

## Introduction
RSA (Rivest-Shamir-Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. Developed in 1977 by Ron Rivest, Adi Shamir, and Leonard Adleman, RSA is based on the computational difficulty of factoring large integers, a problem for which there is no known efficient solution.

## Historical Context
RSA revolutionized the field of cryptography by introducing the concept of a public key for encryption and a private key for decryption. Before RSA, secure communication required the sender and receiver to exchange secret keys in a secure manner, which was a significant limitation.

## How RSA Works

### Key Generation
1. **Select two prime numbers**, $p$ and $q$.
2. **Calculate $n = pq$**. $n$ is used as the modulus for both the public and private keys.
3. **Calculate the totient**, $\phi(n) = (p-1)(q-1)$.
4. **Choose an integer $e$** such that $1 < e < \phi(n)$ and $e$ is co-prime to $\phi(n)$. $e$ is the public key exponent.
5. **Determine $d$** as $d \equiv e^{-1} \mod \phi(n)$. $d$ is the private key exponent.

### Encryption
- Given a plaintext message $M$, the ciphertext $C$ is computed as:
$$C \equiv M^e \mod n$$

### Decryption
- The original message is recovered by computing:
$$M \equiv C^d \mod n$$

## Security
The security of RSA relies on the difficulty of factoring the product of two large prime numbers. As long as this remains computationally infeasible, RSA is considered secure.

## Applications
- Digital Signatures
- Secure Web Browsing (HTTPS)
- Secure Email (PGP, GPG)
- VPNs

## Example
Suppose Alice wants to send a secure message to Bob using RSA:
1. **Bob generates RSA keys** with $p = 61$, $q = 53$.
2. **Bob sends his public key** (n, e) to Alice.
3. **Alice encrypts her message** using Bob's public key and sends it.
4. **Bob decrypts the message** using his private key.

## Conclusion
RSA Public-Key Cryptography is a fundamental algorithm in the field of encryption, enabling secure data transmission and forming the backbone of various internet security protocols.

---

### Test Questions
1. **STARTI [Basic] Question:** What are the two primary components of the RSA algorithm? **Back:** The two primary components of RSA are key generation (involving choosing two prime numbers and computing the public and private keys) and the process of encryption and decryption. **ENDI**
2. **STARTI [Basic] Question:** Why is RSA considered secure? **Back:** RSA's security is based on the difficulty of factoring the product of two large prime numbers, which is a computationally infeasible problem with current technology. **ENDI**
3. **STARTI [Basic] Question:** How does RSA encryption differ from traditional symmetric key encryption? **Back:** Unlike symmetric key encryption, which uses the same key for encryption and decryption, RSA uses a pair of keys – a public key for encryption and a private key for decryption. **ENDI**