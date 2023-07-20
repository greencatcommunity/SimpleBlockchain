import hashlib

class GreenCatBlockchain():
    def __init__(self,hash_previous,data):
        self.hash_previous= hash_previous
        self.data = data
        self.hash = hashlib.sha256((hash_previous+data).encode()).hexdigest()


t1 = GreenCatBlockchain("0","HELLO WORLD")
print(t1.hash)
print(t1.data)
t1 = GreenCatBlockchain(t1.hash,"This is greencat")
print(t1.hash)
print(t1.data)