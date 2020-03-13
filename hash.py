import hashlib, os

def calculateHash(salt, password):
    h = hashlib.new('sha1')
    h.update(('%s%s' % (salt, password)).encode('utf-8'))
    return h.hexdigest()

def generateSalt():
    return os.urandom(32).hex()
    
def checkPassword(salt, hash, enteredPassword):
    return calculateHash(salt, enteredPassword) == hash
