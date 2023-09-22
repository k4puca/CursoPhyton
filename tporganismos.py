# lists

from curses import use_default_colors


logones = ["B959263", "C569853", "T698952","Z698563"]

roles = ["SUPERIOR", "ADJUNTO","TEMPORARIO","TERCERIZADO"]

contraseñas = ["CHIPI1971","EURASIA","JAJAJANT","ECHENME"]



#DEF Usuario Logueado

intentos = 0

def usuarioLogueado():

    LogonIngresado = input ("coloque su logon")
    if LogonIngresado in logones:
        print("Logon autorizado")
    else:
        print("reintente")
        intentos = intentos = + 1
        if intentos > 3:
            print ("intentos agotados")
            terminar()
        else:
            usuarioLogueado()


def rolesAsignados():
    rolElegido = input ("coloque el rol elegido")

    if rolesAsignados in roles:
        print ("rol valido")

    else:
        print ("reintente")

        intentos = intentos = + 1
        if intentos > 3:
            print ("intentos agotados")
            terminar()
        else: usuarioLogueado()
            

def terminar():
    intentos = 3
    print("proceso terminado")


usuarioLogueado()