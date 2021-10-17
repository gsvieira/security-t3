import os, random
def gen_random_int(size:int):
  return os.urandom(size)

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