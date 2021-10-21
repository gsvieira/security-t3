import string, re, sys
def base64_map():
  base64_caracters = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

  map_int_to_char = {}
  map_char_to_int = {}

  for index,char in enumerate(base64_caracters):
    map_int_to_char[index] = char
    map_char_to_int[char] = index

  return (map_char_to_int, map_int_to_char)
  #print(map_char_to_int)

#input
def base64_encoder(str:string):
  #str = "abc"
  bin_input = ''.join('{0:08b}'.format(ord(x), 'b') for x in str)
  print(bin_input)
  bin_list = [bin_input[i:i+6] for i in range(0,len(bin_input), 6)]
  int_list = [int(x, 2) for x in bin_list]
  print(int_list)
  mapping = base64_map()
  retorno = [mapping[1][x] for x in int_list]
  retorno = ''.join(retorno)
  print(retorno)


def base64_decoder(str:string):
  mapping = base64_map()
  int_list = ['{0:06b}'.format(mapping[0][x]) for x in str]
  #print(int_list)
  str = ''.join(int_list)
  bin_list = [str[i:i+8] for i in range(0,len(str), 8)]
  #print(bin_list)
  int_list = [chr(int(x, 2)) for x in bin_list]
  print(int_list)
  return ''.join(int_list)

base64_encoder("abc")
print(base64_decoder("YWJj"))
