from socket import *

servidorNombre = "127.0.0.1" 
servidorPuerto = 12000
clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((servidorNombre,servidorPuerto))


cmd = input("Que desea realizar: ")
mensaje = " "
if(cmd == "saldo"):
    mensaje = cmd
elif(cmd == "debitar" or cmd == "acreditar"):
    monto = input("monto: ")
    try:
        int(monto)
        mensaje = cmd + " " + monto
    except ValueError:
        print("Error monto invalido.")
else:
    raise Exception("Error accion invalida.")

clienteSocket.send(bytes(mensaje, "utf-8"))
mensajeRespuesta = clienteSocket.recv(1024)
print(str(mensajeRespuesta, "utf-8"))
clienteSocket.close()