# Utils es el archivo donde estan las funciones de el ejercicio 3
import utils_e3

ventas = []
def main():
    
    print('Bienvenido al sistema de la LBP del Saman!')

    ans = None
    while ans != 0:

        print('Opciones disponibles:\n1.->Comprar entradas.\n2.->Ver estadisticas.\n3->Salir.\n')
        ans = input('Por favor ingrese su opcion ingresando el numero: \n')
        while not ans.isnumeric() or int(ans) not in range(1,4):
            ans = input('Por favor ingrese una opcion valida: \n')

        if ans == '1':
            utils_e3.imprimir_factura(utils_e3.registrar_cliente(),ventas)
        elif ans == '2':
            utils_e3.estadisticas(ventas)
        elif ans =='3':
            print('Gracias por utilizar nuestro sistema.\n')
            print('Cerrando consola.')
            ans = 0 
            break
    

main()