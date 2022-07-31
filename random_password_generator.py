import random
_pwd=''
for _ in range(0,100):
    #print(chr(random.randint(0,130)))
    #print(chr(_))
    random.seed()
    random.getstate()
    _c=chr(random.randint(33,126))
    _pwd+=_c
print(_pwd)
with open('_pass.txt','w') as _fw:
    _fw.write(_pwd)
    