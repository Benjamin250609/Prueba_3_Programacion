tamaños = ["pequeño","mediano", "grande"]
sectores = ["centro","norte","sur"]


def registrarPedidos(Registro):
    pequeños = 0
    medianos = 0
    grandes = 0

    NombreApellido = input("Ingrese su nombre y su apellido: ")
    direccion = input("Ingrese su direccion: ")
    sector = input("Ingrese su sector: ")
    detalle = input("Ingrese el tamaño de su paquete (Pequeño, Mediano o Grande): ").lower()
    while detalle not in tamaños:
        print("El tamaño ingresado es invalido.")
        detalle = input("Ingrese el tamaño de su paquete (Pequeño, Mediano o Grande): ").lower()
    while detalle in tamaños:
        if detalle == "pequeño":
            pequeños = pequeños + 1
        elif detalle == "mediano":
            medianos = medianos + 1
        elif detalle == "grande":
            grandes = grandes + 1
        continuar = input("¿Desea seleccionar otro tipo de paquete?(s/n): ").lower()
        if continuar == "s":
            detalle = input("Ingrese el tamaño de su paquete (Pequeño, Mediano o Grande): ").lower()
        else:
            break
    Registro.append({"NombreApellido" : NombreApellido,
                     "Direccion" : direccion,
                     "Sector": sector,
                     "Paquetes" : [(f"Pequeños- {pequeños}"), (f"Medianos- {medianos}"), (f"Grandes- {grandes}")]
                     })

def listar_pedidos(registro):
    if registro != []:
        for mostrar in registro:
            for orden in mostrar:
                print(f"{orden} : {mostrar[orden]}")
    else:
        print("No se encuentran datos registrados. ")




def imprimir_hoja(registro):
    if registro != []:
        datos_imprimir = []
        elegir_sector = input("Ingrese unos de los sectores predefinidos(Centro,norte,sur): ").lower()
        while elegir_sector not in sectores:
            print("Sector no valido porfavor selecciones otro: ")
            elegir_sector = input("")
        if elegir_sector == "centro":
            nombreArchivo = "PedidosCentro.txt"
            for sector in registro:
                if sector["Sector"] == "centro":
                    datos_imprimir.append(sector)
        elif elegir_sector == "norte":
            nombreArchivo = "PedidosNorte.txt"
            for sector in registro:
                if sector["Sector"] == "norte":
                    datos_imprimir.append(sector)
        if elegir_sector == "sur":
            nombreArchivo = "PedidosSur.txt"
            for sector in registro:
                if sector["Sector"] == "sur":
                    datos_imprimir.append(sector)
        

        with open(nombreArchivo,"w") as archivo:
            for escribir in datos_imprimir:
                archivo.write(f"Cliente : {escribir["NombreApellido"]}\n")
                archivo.write(f"Direccion : {escribir["Direccion"]}\n")
                archivo.write(f"Sector : {escribir["Sector"]}\n")
                archivo.write(f"Paquetes : {escribir["Paquetes"]}\n")
    else:
        print("No se encuentran datos registrados. ")
                
                





        
            
