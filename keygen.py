import os, random
from timeit import default_timer as timer

def gen_random_int(size:int=128, mask=0):
  x = os.urandom(size)
  x = int.from_bytes(x, "little")
  if mask:
    return x
  #x = (x | (1 << (128*8) -1)) | 1
  return (x | (1 << (128*8) -1)) | 1

def miller_test(odd, num):
  j = 2 + random.randint(1,num - 4)

  #j^odd % num
  x = pow(j, odd, num)

  
  if(x == 1 or x == num - 1):
    return True
  
  while (odd != num - 1):
    x = (x*x) % num
    odd *= 2

    if(x == 1):
      return False
    if(x == num - 1):
      return True
  return False

def is_prime(num, num_of_times):
  #caso base 2,3 são primos, não são aceitos numeros negativos
  if (num<=1 or num == 4):
    return False
  if (num<=3):
    return True
  
  odd = num - 1

  #se o numero for par divide por dois
  while(odd % 2 == 0):
    #usando a divisão // pois python não trabalha bem com float muito grande
    odd = odd // 2

  for i in range(num_of_times):
    if(miller_test(odd, num) == False):
      return False
  
  return True

start = timer()
print(start)
for i in range(20):
  
  while (True):
    prime = gen_random_int()
    if(is_prime(prime,10)):
      break;
  print(i)
end = timer()
print(end - start)
