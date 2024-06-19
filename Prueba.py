import Prueba_funciones as fn

registro = []

while True:
    print("Bienvenido a PaquExpress :D ")

    print("Seleccione una Opcion: ")
    print("1. Registrar pedidos ")
    print("2. Listar pedidos")
    print("3. Imprimir hoja ")
    print("4. salir ")
    
    opcion = input("")

    if opcion == "1":
        fn.registrarPedidos(registro)
        print("Pedido registrado con exito!")
        print("")
    elif opcion == "2":
        fn.listar_pedidos(registro)
        print("")
    elif opcion == "3":
        fn.imprimir_hoja(registro)
        if registro != []:
            print("Hoja creada con exito!")
        print("")
    elif opcion == "4":
        print("Saliendo.....")
        break


