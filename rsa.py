#fix keys and make AES 
from Crypto.Cipher import AES
import keygen,string, hashlib, base_64

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


key = True

if __name__ == '__main__':
    if key == True:
        key = keygen.gen_key_pair()
        with open("rsa_key/rsa.pub.txt", "w") as f:

            f.write(str(key[0][0])+' '+str(key[0][1]))
        f.close
        with open("rsa_key/rsa.txt", "w") as f:
            f.write(str(key[1][0])+' '+str(key[1][1]))
        f.close
    with open("rsa_key/rsa.pub.txt", "r") as f:
        file_pub = f.read()
    with open("rsa_key/rsa.txt", "r") as f1:
        file_priv = f1.read()

    public_key = file_pub.split(" ")
    public_key = [int(x) for x in public_key]
    """ print(file_pub)
    print(file_priv)
    print(public_key) """
    

    cipher = encode_char(public_key, "hello")
    #print(cipher)
    cipher = [str(x) for x in cipher]
    #print(cipher)
    priv_key = file_priv.split(" ")
    priv_key = [int(x) for x in priv_key]
    #print(priv_key)
    msg = decode_char(public_key, priv_key, cipher)
    print(msg)

    #assinatura
    