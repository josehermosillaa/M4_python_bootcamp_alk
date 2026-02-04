#2 readline
archivo = open('accesos.log', 'r')
contador = 0
login_ok = 0
login_fail = 0
while True:
    contador += 1
    linea = archivo.readline()
    
    if not linea: #no existe la linea, esdecir archivo.readline() == None
        archivo.close()
        break

    iterable = linea.strip().split(';')
    estado_login = iterable[2]
    if estado_login == "LOGIN_OK":
        login_ok  = login_ok + 1
    elif estado_login == "LOGIN_FAIL":
        login_fail += 1
    
    print(f"linea {contador}", linea)

print("LOGIN_OK: ", login_ok )
print("LOGIN_FAIL: ", login_fail )