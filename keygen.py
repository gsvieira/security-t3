import os, random, sys, math
from timeit import default_timer as timer

def gen_random_int(size:int=128, mask=0):
  x = os.urandom(size)
  x = int.from_bytes(x, "little")
  if mask:
    return x
  #x = (x | (1 << (128*8) -1)) | 1
  return (x | (1 << (size*8) -1)) | 1



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

def gen_prime_number():
  while (True):
    prime = gen_random_int()
    if(is_prime(prime,10)):
      return prime
  
def phi(num:int):
  return num - 1

def mdc(n1,n2):
  resto = 1
  while (n2!=0):
    resto = n1%n2
    n1 = n2
    n2 = resto
  return n1

def gen_E(num):
  while True:
    e = random.randrange(2,num)
    if (mdc(num,e) == 1):
      return e

def gen_D(phi, e):
  if(math.gcd(e,phi)!=1):
    return None
  #retorna inverso multiplicativo no modulo
  return pow(e, -1, phi)

def gen_key_pair(p=0,q=0):
  start = timer()
  if(p==0 or 1 == 0):
    p = gen_prime_number()
    q = gen_prime_number()
  n=p*q
  """ print(p)
  print(q) """
  phi_N = phi(p)*phi(q)

  e = gen_E(phi_N)
  public_key = (e, n)
  print("Essa é sua chave publica: ", public_key)
  d = gen_D(phi_N,e)
  print("Essa é sua chave privada: ", d)
  end = timer()
  print(end - start)
  #retorna chave publica (e,n) e chave privada(d,n)
  return (public_key, (d, public_key[1]))


if __name__ == '__main__':
  if (len(sys.argv)<=2 or len(sys.argv)>=4):
    gen_key_pair()
  else:
    gen_key_pair(int(sys.argv[1]), int(sys.argv[2]))

""" 
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
 """


