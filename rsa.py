#fix keys and make AES 
from Crypto.Cipher import AES
import keygen,string, hashlib, base_64, sys

def encode_char(public_key, str:string):
    result = []
    for index, char in enumerate(str):
        #print(index)
        result.append(pow(ord(char), public_key[0],public_key[1]))
    return result

def decode_char(public_key, priv_key, cipher):
    return "".join([chr(pow(int(x), priv_key[0], public_key[1])) for x in cipher])

    #cifra a chave simetrica
def encode_block(public_key, block:string):
    number_str = base_64.decoder(block)
    num = int(number_str)
    block_cipher = pow(num, public_key[0], public_key[1])
    return base_64.encoder(str(block_cipher))
    
    #decifra a chave simetrica
def decode_block(public_key, priv_key, block:string):
    number_str = base_64.decoder(block)
    num = int(number_str)
    block_cipher = pow(num, priv_key[0], public_key[1])
    return base_64.encoder(str(block_cipher)) 

def aes_cipher(msg, encoded_aes_key, padding_char):
    aes_key = base_64.decoder(encoded_aes_key)
    cipher = AES.new(aes_key)
    padded_msg = msg + (padding_char * ((16-len(msg)) % 16))
    ciphered_msg = cipher.encrypt(padded_msg)
    return base_64.encoder(ciphered_msg)

def aes_decipher(encoded_ciphered_msg, encoded_aes_key, padding_char):
    aes_key = base_64.decoder(encoded_aes_key)
    ciphered_msg = base_64.decoder(encoded_ciphered_msg)
    cipher = AES.new(aes_key)
    deciphered_msg = cipher.decrypt(ciphered_msg)
    unpadded_msg = deciphered_msg.rstrip(padding_char)
    return unpadded_msg

if __name__ == '__main__':
    if(len(sys.argv)==2):
        if sys.argv[1] == '-g':
            key = keygen.gen_key_pair()
            aes_key = keygen.gen_symetric_key()

            with open("rsa_key/rsa.pub.txt", "w") as f:
                f.write(key[0][0]+' '+key[0][1])
            f.close

            with open("rsa_key/rsa.txt", "w") as f:
                f.write(key[1])
            f.close

            with open("aes_key.txt", "w") as f:
                f.write(aes_key)
            f.close

    with open("rsa_key/rsa.pub.txt", "r") as f:
        file_pub = f.read()
    with open("rsa_key/rsa.txt", "r") as f1:
        file_priv = f1.read()
    with open("aes_key.txt", "r") as f2:
        aes_key = f2.read()

    public_key = file_pub.split(" ")
    public_key = [int(base_64.decoder(x)) for x in public_key]
    """ print(file_pub)
    print(file_priv)
    print(public_key) """
    

    cipher = encode_char(public_key, "hello")
    #print(cipher)
    cipher = [str(x) for x in cipher]
    #print(cipher)
    priv_key = file_priv.split(" ")
    priv_key = [int(base_64.decoder(x)) for x in priv_key]
    #print(priv_key)
    msg = decode_char(public_key, priv_key, cipher)
    print(msg)
    ciphered_msg = aes_cipher(msg, aes_key, ":")
    deciphered_msg = aes_decipher(ciphered_msg, aes_key, ":")
    print(ciphered_msg)
    print(deciphered_msg)

    #assinatura
    