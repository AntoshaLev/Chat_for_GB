# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
import binascii

strs = [b'class', b'function', b'method']

for s in strs:
    print(type(s), binascii.hexlify(s), len(s))

# <class 'bytes'> b'636c617373' 5
# <class 'bytes'> b'66756e6374696f6e' 8
# <class 'bytes'> b'6d6574686f64' 6
