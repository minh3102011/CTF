from Crypto.PublicKey import RSA
f = open('/home/bien/Downloads/privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a.pem', 'r')
flag = RSA.importKey(f.read())
print(flag.d)
