entradas = [{'tipo': 'GEN', 'precio': 45},{'tipo': 'VIP', 'precio': 65} ]

def registrar_cliente():

    name = input('Por favor ingrese su nombre: ')
    while not name.isalpha() or len(name) > 20:
        name = input('Por favor ingrese un nombre valido(No se aceptan numeros ni nomrbes mayoes a 20 caracteres: \n)')

    ced = input('Por favor ingrese su cedula: ')
    while not ced.isnumeric() or len(ced) > 8:
        ced = input('Por favor ingrese unacedula valida: \n)')    

    # No se valida el correo porque no esta especificado en el enunciado del ejercicio
    cor = input('Por favor ingrese su correo: ')
    while not '@' in cor:
        cor = input('Por favor ingrese una direccion de correo valida(Al menos un "@": )')

    tick = input('Por favor ingrese el codigo de su entrada: "VIP/GEN"\n')
    while not tick.isalpha() or tick.upper() not in ['GEN','VIP']:
        tick = input('Por favor ingrese un codigo valido "VIP/GEN": \n')

    tick = tick.upper()

    amm = input('Por favor ingrese la cantidad de entradas que desea comprar(Maximo 10 por compra): \n')
    while not amm.isnumeric() or int(amm) not in range(1,11):
        amm = input('Por favor ingrese un numero entre 1 y 10: \n') 

    return {'name': name, 'ced': ced, 'mail': cor, 'tick': tick, 'amm': int(amm)}
    
def imprimir_factura(datos, ventas):

    tip = datos['amm']
    cod = datos['tick']

    dsc = False
    for tipo in entradas: 
        if datos['tick'] == tipo['tipo'] and tipo['tipo']=='VIP':
            subt = datos['amm']*tipo['precio']
            anovrguesas = 2*datos['amm']
            print(f'Entrada VIP.\nAcceso a areas exclusivas y {anovrguesas} hamburguesas de regalo!\n')
            datos['burgir'] = anovrguesas
        elif datos['tick'] == tipo['tipo'] and tipo['tipo']=='GEN':
            subt = datos['amm']*tipo['precio']

    if datos['amm']%2 != 0:
        subt -= subt*0.1
        dsc = True
        print('Cliente con descuento por cantidad de entradas impar!\n')

    print(f'Entradas en total: {tip} del tipo: {cod}\nSubtotal: {subt}')
    ans = input('Desea confirmar el pago?Y/N: ')
    while not ans.isalpha() or ans.upper() not in ['Y','N']:
        ans = input('Ingrese una opcion valida (Y/N): \n')
    
    if ans.upper()  == 'N':
        print('Compra cancelada, volviendo al menu principal.\n')
        pass
    elif ans.upper() == 'Y':    
        datos['dsc'] = dsc
        ventas.append(datos)
        print('Compra registrada y cliente anadido!')
        print(datos)
        print(ventas)

def estadisticas(ventas):
    counter_vip = 0
    counter_gen = 0
    counter_dsc = 0
    for venta in ventas: 
        if venta['tick'] == 'VIP':
            counter_vip += 1
        elif venta['tick'] == 'GEN':
            counter_gen += 1

    for venta in ventas: 
        if venta['dsc'] == True:
            counter_dsc += 1

    print(f'Descuentos otorgados hasta el momento: {counter_dsc}.\nCompras en general: {counter_gen}.\nCompras en VIP: {counter_vip}.')
    
    



    
        


