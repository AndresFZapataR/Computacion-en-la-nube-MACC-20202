from socket import *

def saldo():
    arch = open('saldo.txt','r+')
    sal = arch.readline()
    arch.close()
    return sal

def debitar(X):
    arch = open('saldo.txt','r+')
    sal = int(arch.readlines()[0])
    arch.seek(0)
    if X > sal:
        arch.close()
        return 'Saldo insuficiente'
    else:
        sal -= X
        arch.write(str(sal))
        arch.close()
        return 'OK'

def acreditar(Y):
    arch = open('saldo.txt','r+')
    sal = int(arch.readlines()[0])
    arch.seek(0)
    sal+=Y
    arch.write(str(sal))
    arch.close()
    return 'Nuevo saldo: {}'.format(str(sal))

servidorPuerto = 12000
servidorSocket = socket(AF_INET,SOCK_STREAM)
servidorSocket.bind(('',servidorPuerto))
servidorSocket.listen(1)
print('El servidor está listo para recibir mensajes...')
while 1:
    conexionSocket, clienteDireccion = servidorSocket.accept()
    print('Conexión establecida con ', clienteDireccion)
    mensaje = str( conexionSocket.recv(1024), "utf-8" )
    print('Mensaje recibido de ', clienteDireccion)
    print(mensaje)
    mensajeRespuesta = ' '
    if(mensaje == 'saldo'):
        mensajeRespuesta = 'Su saldo actual es de $' + saldo()
    else:
        m = mensaje.split(' ')
        try:
            monto = int(m[1])
            print(monto)
            if(m[0] == 'acreditar'):
                mensajeRespuesta = acreditar(monto)
            elif(m[0] == 'debitar'):
                mensajeRespuesta = debitar(monto)
            else:
                mensajeRespuesta = 'Consulta o transferencia invalida'
        except:
                mensajeRespuesta = 'Monto invalido'
    print(mensajeRespuesta)
    conexionSocket.send(bytes(mensajeRespuesta, 'utf-8'))
    conexionSocket.close()