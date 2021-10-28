import string, re, sys
def base64_map():
  base64_caracters = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

  map_int_to_char = {}
  map_char_to_int = {}

  for index,char in enumerate(base64_caracters):
    map_int_to_char[index] = char
    map_char_to_int[char] = index

  return (map_char_to_int, map_int_to_char)

#input
def encoder(str:string):
  #padding when lenght isn't multiple of 3
  while(len(str)%3!=0):
    str+=' '
  
  bin_input = ''.join('{0:08b}'.format(ord(x), 'b') for x in str)
  #print(len(bin_input))
  int_list = [int(bin_input[i:i+6], 2) for i in range(0,len(bin_input), 6)]
  #int_list = [int(x, 2) for x in bin_list]
  #print(int_list)
  mapping = base64_map()
  return ''.join([mapping[1][x] for x in int_list])
  


def decoder(str:string):
  mapping = base64_map()
  int_list = ['{0:06b}'.format(mapping[0][x]) for x in str]
  #print(int_list)
  str = ''.join(int_list)
  bin_list = [str[i:i+8] for i in range(0,len(str), 8)]
  #print(bin_list)
  int_list = [chr(int(x, 2)) for x in bin_list]
  #print(int_list)
  return ''.join(int_list).strip()

def b_encoder(byteArr:bytes):
  while(len(byteArr)%3!=0):
    byteArr = byteArr+ b'\x00'
  #print(byteArr)
  bin_input = ''.join(format(byte, '08b') for byte in byteArr)
  int_list = [int(bin_input[i:i+6], 2) for i in range(0,len(bin_input), 6)]
  mapping = base64_map()
  return ''.join([mapping[1][x] for x in int_list])

def b_decoder(str:string):
  mapping = base64_map()
  int_list = ['{0:06b}'.format(mapping[0][x]) for x in str]
  byte_str = ''.join(int_list)
  #elimina o padding
  byte_str = byte_str[:128]
  bin_list = [byte_str[i:i+8] for i in range(0,len(byte_str), 8)]
  #print(bin_list)
  int_list = [int(x, 2).to_bytes(1,'big') for x in bin_list]
  #print(int_list)
  #print(b_result)
  return b"".join(int_list)

#main
if(__name__ == '__main__'):
  #print(base64_encoder("I Am Joh"))
  #print(list(decoder(encoder("I Am John"))))
  test = b'\xe1\xc5\x8f\xc1Z \x11\x0c\x95\t P\xb8k\x81\xb5'
  print(b_decoder(b_encoder(test)))
