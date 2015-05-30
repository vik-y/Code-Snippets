class client:
    def __init__(self, clientName, privateKey, publicKey):
        self.clientName = clientName
        self.private_key = privateKey
        self.public_key = publicKey
        self.decryptionKey = 0;
    
    def displayKeys(self):
        print self.private_key
        print self.public_key
    
    def encryptMessage(self, message, client):
        print self.clientName, "is encrypting message: ", message, ": for ", client.clientName
        pubKey = client.getPublicKey()
        encrypted = (message**pubKey[1])%pubKey[0]
        print encrypted
        return encrypted
        
    def decryptMessage(self, eMessage):
        print self.clientName, "is decrypting message: ", eMessage
        if(self.decryptionKey==0): 
            print "Error, no decryption key defined"
        else: 
            decrypted = (eMessage**self.decryptionKey)%(self.public_key*self.private_key)
            print decrypted
            return decrypted
        
    def getPublicKey(self):
        n = self.private_key*self.public_key 
        fn = (self.private_key-1)*(self.public_key-1) #phi(n)
        pExponent, k = 3, 2
        d = (k*fn+1)/pExponent
        self.decryptionKey = d;
        return (n,pExponent)
        
        
client1 = client("client1", 101, 179)
client2 = client("client2", 53, 59)


client2.decryptMessage(client1.encryptMessage(89, client2))
