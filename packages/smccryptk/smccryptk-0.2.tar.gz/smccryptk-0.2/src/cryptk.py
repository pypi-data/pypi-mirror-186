
""" File containing all cryptk library module for secure multiparty computation over a distributed network. """

# ~ Libraries used
# pip3 install pycrypto
# pip3 install rsa

# Cryptk/cryptk
from Crypto.Cipher import AES
import rsa
import hashlib



class Cryptk:
    
    key_size = 128
    iv_size = 16

    # Privates
    _keystring_magic = ':~:'
    _pad_chr = '\0' # pad msg with this character if needed
    

    def __init__(self):
        # Generate new rsa keys
        public, private = rsa.newkeys(Cryptk.key_size*8) # Multiply by 8 to get size in bits
        self.private_key = private
        self.public_key = public

        # Privates
        self._keystring_magic = ':~:'
        self._encrypt_pkey = True # If sender should add its own public key to the blob sent
        
    
    def key2string(key):
        """ Converts key object to string, in order to send it easily over http and reconstruct it on the receiving side. """
        n = key.n
        e = key.e
        return "%d%s%d" % (n, Cryptk._keystring_magic, e)
    
    def string2key(strkey):
        """ Converts string to key object defined within rsa library """
        n, e = strkey.split(Cryptk._keystring_magic)
        return Cryptk.construct_key(int(n), int(e))
    
    def get_keysize(self):
        # Returns key size for public and private key in bytes.
        return Cryptk.key_size
    
    def get_public_key(self):
        return self.public_key


    def generate_key(self, key_size):
        """ Generates new random (usually 16 bytes) symmetric key, unique for each message sent """
        # New symmetric key
        # Length should be either 16, 24, 32 bytes
        # from https://stuvel.eu/python-rsa-doc/usage.html#generating-keys
        return rsa.randnum.read_random_bits(key_size*8) # Multiply by 8 to convert bytes to bits
    
    def construct_key(n, e):
        # Constructs key object from n and e
        return rsa.PublicKey(n, e)
    

    def encrypt(self, to_user_pkey, str_msg):
        """ 
        Encryption:
            Generate symmetric key used to crypt the data message.
            Encrypt the data message with the symmetric key.
            Encrypt the symmetric key on users public available key.
        Returns: 
            Public-key-size(4 bytes) + IV + public-key + signature + key + data as a byte stream which has been encrypted to user.
        params:
            @to_user_pkey: users public key
            @msg: msg to encrypt """
        
        # Pad message as it must be a multiple of 16
        padded_msg = Cryptk.Pad_message(str_msg)

        # Symmetric key used to encrypt/decrypt the message
        symmetric_key = self.generate_key(16) # size must be either 16, 24 or 32 bytes
        sendIV = self.generate_key(16)

        AES_obj = AES.new(symmetric_key, AES.MODE_CBC, sendIV)
        encrypted_msg = AES_obj.encrypt(padded_msg.encode("UTF-8"))
        

        encrypted_key = rsa.encrypt(symmetric_key, to_user_pkey)

        signature = self.sign(str_msg.encode())

        # Send own public key with the message as well
        pk = b''
        if self._encrypt_pkey:
            pk = Cryptk.key2string(self.get_public_key()).encode()
        
        pk_size = len(pk).to_bytes(4, 'little')

        return pk_size + sendIV + pk + signature + encrypted_key + encrypted_msg
    

    def decrypt(self, cipher):
        """
        Decrypton:
            Decrypt the secret key.
            Decrypt the data message based on the secret key.
        params:
            @cipher: contains public key size, IV, public-key, signature, encrypted symmetric key and encrypted message, respectively """

        # Get sizes in bytes
        iv_size = Cryptk.iv_size
        keysize = self.get_keysize()

        # Retrieve data from stream
        pk_size = int.from_bytes(cipher[:4], 'little') # First 4 bytes is the size of the senders public key (this varies so sending the size is needed)
        recvIV = cipher[4:iv_size+4]
        senders_pkey = cipher[iv_size+4:pk_size+iv_size + 4]
        signature = cipher[4+pk_size+iv_size:pk_size + iv_size + keysize+4]
        encrypted_key = cipher[4+pk_size + iv_size + keysize:pk_size + iv_size + keysize*2 + 4]
        encrypted_msg = cipher[4 + pk_size + iv_size + keysize*2:]

        if self._encrypt_pkey:
            senders_pkey = Cryptk.string2key(senders_pkey.decode())

        symmetric_key = rsa.decrypt(encrypted_key, self.private_key)

        AES_obj = AES.new(symmetric_key, AES.MODE_CBC, recvIV)
        msg = AES_obj.decrypt(encrypted_msg)
        # Remove padding on message
        msg = Cryptk.Remove_pad(msg.decode())

        # Verify message authentication from sender
        # This is to make sure the message has not been altered during transmission
        self.verify(senders_pkey, msg.encode(), signature)

        return msg
    
    def Pad_message(msg):
        """ Pad message to a multiple of 16 bytes. Returns the padded message. """
        # Pads message with '*'
        length = len(msg)
        pad = abs(length%(-16)) + length
        return msg.ljust(pad, Cryptk._pad_chr)

    
    def Remove_pad(msg):
        """ Remove message padding if any. Returns the non padded message """
        ls = msg.split(Cryptk._pad_chr)
        if len(ls) > 1:
            # In case the msg contains any '_pad_chr' that isn't padded,
            # we only remove the last sequence of '_pad_chr'
            del ls[-1]
            sumls = ""
            for i in ls:
                sumls += i
            return sumls
        else:
            return ls[0]
    
    def get_hash(self, msg):
        m = hashlib.sha256()
        m.update(msg)
        return m.hexdigest()
    
    
    def sign(self, msg):
        # Sign by hashing the message and encrypting it with the secret key.
        # Anyone with the public key can decrypt and compare the hashed value
        # to verify that the message is from the correct sender and hasn't been altered during transmission.
        signature = rsa.sign(msg, self.private_key, 'SHA-256')
        return signature
    
    def verify(self, key, msg, signature):
        # Use the senders public key to verify the message
        try:
            rsa.verify(msg, signature, key)
        except:
            print("Verification on msg failed")
            return False
        return True


