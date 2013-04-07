This is the beginnings of a cryptographic that will increase overall strength of an associated cryptographic algorithm.  
It certainly works in its own right but works better when combined with other encryption algorithms.  

Examples include but are not limited to:
  -RSA
  -DES
  -Blowfish
  
Basic premise:

The algorithm currently adds padding to plaintext in such a way that makes cryptanalysis more difficult.  This is because it pads based on a given corpus (chosen by the encrypter) and mimics that frequency.  This makes discerning the true plaintext difficult.  In order decrypt, you need a series of offsets, for each actual plaintext character.  By combining both of these, we have an easy to decrypt and relatively cheap encryption algorithm.

The main strength of this algorithm is its ability to be used in conjunction with other algorithms as well as the potential for fast encryption and decryption.  This makes it ideal for use within other standards, thus increasing overall toughness of any encryption standard.

How to use:
------------------------------------------------------------------------------------------------------------------------
