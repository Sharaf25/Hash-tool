import hashlib

choose = input("1- Hash plain text\n2- Compare hash\n")
if(choose=='1'):
   Pt=input("Enter plain text:\n")
   cha=input("choose Hashing algorithm:\n1- MD5\n2- SHA1\n3- SHA384\n4- SHA224\n5- SHA256\n6- SHA512\n")
   if(cha=='1' or cha=="MD5" or cha=="md5"):
      print(hashlib.md5(Pt.encode()).hexdigest())
   elif(cha=='2' or cha=="SHA1" or cha=="sha1"):
       print(hashlib.sha1(Pt.encode()).hexdigest())
   elif(cha=='3' or cha=="SHA384" or cha=="sha384"):
       print(hashlib.sha384(Pt.encode()).hexdigest())
   elif(cha=='4' or cha=="SHA224" or cha=="sha224"):
       print(hashlib.sha224(Pt.encode()).hexdigest())
   elif(cha=='5' or cha=="SHA256" or cha=="sha256"):
       print(hashlib.sha256(Pt.encode()).hexdigest())
   elif(cha=='6' or cha=="SHA512" or cha=="sha512"):
       print(hashlib.sha512(Pt.encode()).hexdigest())
elif(choose=='2'):
 plaintext = input("Enter the plain text:\n")
 ciphertext = input("Enter the cipher text:\n")

 md5 = hashlib.md5(plaintext.encode())
 sha1 = hashlib.sha1(plaintext.encode())
 sha384 = hashlib.sha384(plaintext.encode())
 sha224 = hashlib.sha224(plaintext.encode())
 sha256 = hashlib.sha256(plaintext.encode())
 sha512 = hashlib.sha512(plaintext.encode())


 fin0=md5.hexdigest()
 fin1=sha1.hexdigest()
 fin2=sha384.hexdigest()
 fin3=sha224.hexdigest()
 fin4=sha256.hexdigest()
 fin5=sha512.hexdigest()

 if(ciphertext==fin0): 
   print ("The plain text you entered is hashed by MD5")
 elif(ciphertext==fin1):
   print ("The plain text you entered is hashed by SHA1")
 elif(ciphertext==fin2):
   print ("The plain text you entered is hashed by SHA384")
 elif(ciphertext==fin3):
   print ("The plain text you entered is hashed by SHA224")
 elif(ciphertext==fin4):
   print ("The plain text you entered is hashed by SHA256")
 elif(ciphertext==fin5):
   print ("The plain text you entered is hashed by SHA512")
 else :
   print ("Plain text doesn't match cipher text !")