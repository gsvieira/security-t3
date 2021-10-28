#hash ang signature
from Crypto.Cipher import AES
import keygen,string, hashlib, base_64, sys

def cipher_rsa_char(public_key, str:string):
    result = []
    for index, char in enumerate(str):
        #print(index)
        result.append(pow(ord(char), public_key[0],public_key[1]))
    return result

def decipher_rsa_char(public_key, priv_key, cipher:string):
    return "".join([chr(pow(int(x), priv_key[0], public_key[1])) for x in cipher])

    #cifra a chave simetrica
def cipher_rsa_block(public_key, block:string):
    number_str = base_64.b_decoder(block)
    #print(number_str)
    num = int(number_str)
    block_cipher = pow(num, public_key[0], public_key[1])
    return base_64.encoder(str(block_cipher))
    
    #decifra a chave simetrica
def decipher_rsa_block(public_key, priv_key, block:string):
    number_str = base_64.b_decoder(block)
    #print(number_str)
    num = int(number_str)
    block_cipher = pow(num, priv_key[0], public_key[1])
    return base_64.encoder(str(block_cipher)) 



def b_cipher_block(public_key, block:string):
    number_str = base_64.b_decoder(block)
    print(number_str)
    num = int.from_bytes(number_str, "big")
    block_cipher = pow(num, public_key[0], public_key[1])
    return base_64.encoder(str(block_cipher))
    
    #decifra a chave simetrica
def b_decipher_block(public_key, priv_key, block:list):
    number_str = base_64.decoder(block)
    print(number_str)
    num = int(number_str)
    block_cipher = pow(num, priv_key[0], public_key[1])    
    return base_64.encoder(str(block_cipher)) 



def aes_cipher(msg, encoded_aes_key, padding_char):
    aes_key = base_64.b_decoder(encoded_aes_key)
    cipher = AES.new(aes_key)
    padded_msg = msg + (padding_char * ((16-len(msg)) % 16))
    ciphered_msg = cipher.encrypt(padded_msg)
    return base_64.b_encoder(ciphered_msg)

def aes_decipher(encoded_ciphered_msg, encoded_aes_key, padding_char):
    aes_key = base_64.b_decoder(encoded_aes_key)
    ciphered_msg = base_64.b_decoder(encoded_ciphered_msg)
    #print(ciphered_msg)
    cipher = AES.new(aes_key)
    deciphered_msg = cipher.decrypt(ciphered_msg)
    #print(deciphered_msg)
    unpadded_msg = deciphered_msg.decode("utf-8").rstrip(padding_char)
    return unpadded_msg

if __name__ == '__main__':
    if(len(sys.argv)==2):
        if sys.argv[1] == '-g':
            key = keygen.gen_key_pair()
            #aes_key = keygen.gen_symetric_key()

            with open("rsa_key/rsa.pub.txt", "w") as f:
                f.write(key[0][0]+' '+key[0][1])
            f.close

            with open("rsa_key/rsa.txt", "w") as f:
                f.write(key[1])
            f.close

            """ with open("aes_key.txt", "w") as f:
                f.write(aes_key)
            f.close """

    with open("rsa_key/rsa.pub.txt", "r") as f:
        file_pub = f.read()
    with open("rsa_key/rsa.txt", "r") as f1:
        file_priv = f1.read()
    """ with open("aes_key.txt", "r") as f2:
        aes_key = f2.read() """
    with open("msg.txt", "r") as f3:
        mensagem = f3.read()
    #preparação das chaves
    public_key = file_pub.split(" ")
    public_key = [int(base_64.decoder(x)) for x in public_key]
    priv_key = file_priv.split(" ")
    priv_key = [int(base_64.decoder(x)) for x in priv_key]
    #cifragem

    cipher = cipher_rsa_char(public_key, mensagem)
    cipher = [str(x) for x in cipher] #when return a int
    encoded_cipher = [base_64.encoder(x) for x in cipher]
    cipher = "::::".join(encoded_cipher)
    #print(msg)
    #ciphered_msg = aes_cipher(mensagem, aes_key, ":")
    #print(ciphered_msg+"\n")
    
    with open("output/ciphered_msg.txt", "w") as f:
        f.write(cipher)
    f.close

    #assinatura
    """processo de decifrar a mensagem (ponto de vista do destinatário(dono da chave privada) da mensagem)"""

    with open("output/ciphered_msg.txt", "r") as f:
        ciphered_msg = f.read()
    f.close

    encoded_arr_char = ciphered_msg.split("::::")
    arr_char = [base_64.decoder(x) for x in encoded_arr_char]
    deciphered_msg = decipher_rsa_char(public_key, priv_key, arr_char)
    print(deciphered_msg)
    """ with open("output/ciphered_msg.txt", "r") as f3:
        mensagem = f3.read()

    aes_key_ciphered = mensagem[:208]
    print(aes_key_ciphered+"\n")
    aes_key_deciphered = b_decipher_block(public_key, priv_key, aes_key_ciphered)
    print(aes_key_deciphered) 
    deciphered_msg = aes_decipher(mensagem[208:], aes_key_deciphered, ":")"""