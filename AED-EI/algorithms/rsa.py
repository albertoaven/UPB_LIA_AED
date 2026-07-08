def gcd(a, b):
  while b:
    a, b = b, a % b

  return a


def mod_inverse(e, phi):
  for d in range(2, phi):
    if (e * d) % phi == 1:
      return d

  return None

def generate_keys():
  """
  Generación educativa de claves RSA.

  Utiliza números primos pequeños.
  """

  p = 61
  q = 53

  n = p * q

  phi = (p - 1) * (q - 1)

  e = 17

  d = mod_inverse(e, phi)

  public_key = (e, n)
  private_key = (d, n)

  return (public_key,private_key)

def encrypt(message, public_key):
  e, n = public_key

  encrypted = []

  for char in message:
    encrypted.append(
      pow(ord(char), e, n)
    )

  return encrypted

def decrypt(cipher, private_key):
  d, n = private_key

  message = ""

  for value in cipher:
    message += chr(
      pow(value, d, n)
    )

  return message