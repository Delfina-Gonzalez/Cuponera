import random, string
from datetime import datetime

def cuponera(user):
    """Esta funcion genera cupones aleatorios"""
    # calculo fecha actual y la formateo a str
    current_date = datetime.now().date()
    date_str = current_date.strftime("%Y-%m-%d").replace("-", "")
    
    # aseguro longitud del cupon y defino parte aleatoria
    longitud_30 = 28-len(user)-len(date_str)
    todos_los_caracteres = string.ascii_uppercase + string.digits
    aleatorios = ''.join(random.choice(todos_los_caracteres) for _ in range(longitud_30))

    #retorno cupon
    return str(user.upper() + "-" + date_str + "-" +  aleatorios)

ok = False
while not ok:
    user = input("\n\tIngrese su usuario: ")
    if 0<len(user.strip(" "))<16:
        ok = True
        print("\n\tCupon: " + cuponera(user) + "\n\tLongitud: " + str(len(cuponera(user))))
    else:
        print("Usuario invalido, intente de nuevo")