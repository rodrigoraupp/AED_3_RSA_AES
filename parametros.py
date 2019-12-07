#algoritmo que computa a chave pública e retorna N e E referentes aos parâmetros RSA
from Crypto.PublicKey import RSA
key = RSA.importKey(open('rsa.pub').read())
print (key.n, key.e)
