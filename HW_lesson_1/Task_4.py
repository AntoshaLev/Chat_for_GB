# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).
import chardet

strs = ['разработка', 'сокет', 'декоратор']
strs_in_bytes = []

for s in strs:
    s = s.encode('utf-8', errors='namereplace')
    strs_in_bytes.append(s)
    print(s)


# b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
# b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
# b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

for s in strs_in_bytes:
    print(s.decode('ascii', errors='replace'))
    print(s.decode(chardet.detect(s)['encoding']))

# ��������������������
# разработка
# ����������
# сокет
# ������������������
# декоратор


