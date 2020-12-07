import hashlib

with open("replace","r") as file1:
        passwordL = [line.rstrip() for line in file1] 

response="replace"

for i in passwordL:
    authstr = "master:ManagementRealm:" + i
    h1=hashlib.md5(authstr).hexdigest()
    h2=hashlib.md5("replace").hexdigest()
    nonce="replace"
    cnonce="replace"
    nc="replace"
    qop="replace"
    rs = h1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + h2
    response1=hashlib.md5(rs).hexdigest()
    if response1 == response:
        print i
        exit
