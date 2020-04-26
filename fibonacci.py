import base64
import socket

# функция для приёма данных
def recv_unill(s, end=b"\n"):
    ba = bytearray()

    while True:
        data = s.recv(1)
        if not data:
            raise RuntimeError('Server closed socket prematurely')
        ba += data
        if ba.endswith(end):
            break
    return ba.decode("utf-8")

# шифр цезаря
def ceasar(a, key):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = str(a)[2:-1]
    new = ''

    for i in range(len(a)):
        if a[i] in abc or a[i] in ABC:
            if a[i] in abc:
                new += abc[(abc.find(a[i])+key)%26]
            else:
                new += ABC[(ABC.find(a[i])+key)%26]
        else:
            new += a[i];

    return new.encode()

# конектимся
HOST = "212.26.237.212"
PORT = 4444
s = socket.socket()
s.connect((HOST, PORT))
print('connected: ', HOST)

# это та самая первая строчка с иероглифами
res = recv_unill(s)
print(res)

# три переменные для чисел Фибоначчи
a = 0
b = 1
c = 1
count = 1 # Во-первых, это Счётчик
          # Во-вторых, это индикатор (обрезать полученное сообщение или нет)
          # у первой Base64-строчки нет >>> в отличие от остальных

while True :

# принимаем данные + если надо, обрезаем
    if count == 1 :
        res = recv_unill(s)
    else:
        res = recv_unill(s)
        res = res[3:]
    print('То, что мы получаем: ', res)
    if 'flag' in res:
        print('МЫ ЭТО СДЕЛАЛИ!!!')
        break

# отправляем преобразованную строчку
    msg = base64.b64decode(res.encode())
    if count == 1:
        s.send(msg)
        print('Счётчик: ', count, ' То, что мы отправляем: ', msg.decode('utf-8'))
    else:
        
# считаем очередное число Фибоначчи
        c = a + b
        a = b
        b = c
        s.send(ceasar(msg, -a%26))
        print('Счётчик: ', count, ' То, что мы отправляем: ', ceasar(msg, -a).decode('utf-8'))

    count += 1
