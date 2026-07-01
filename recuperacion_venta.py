### Calculo de venta con descuento
def calcular_descuento(subtotal):
    if subtotal:
        if 50000 <= subtotal:
            return subtotal * 0.10
        else:
            return 0

def mostrar_resultado(nombre_producto,subtotal,descuento,total):
    print("--- Venta ---")
    print(f"Producto: {nombre_producto}")
    print(f"Subtotal: {subtotal}")
    print(f"Descuento: {descuento}")    
    print(f"Total a pagar: {total}")

### Programa principal
cond = True

while cond:
    #### ENTRADA
    nombre_producto = str(input("Ingrese en nombre del producto: "))
    if nombre_producto and nombre_producto != "":
        ### Verificacion de precio producto
        try: 
            precio_unitario= int(input("Ingrese precio del producto: "))
            if precio_unitario <= 0 or precio_unitario == "":
                raise ValueError
        except ValueError:
            print("Error! precio debe ser NUMERICO")
            continue

        try:
            cantidad_comprada = int(input("Ingrese la cantidad del producto: "))
            if cantidad_comprada <= 0 or cantidad_comprada == "":
                raise ValueError
        except ValueError:
            print("Error! cantidad debe ser un NUMERO ENTERO mayor que cero")
            continue

        #### PROCESO
        # calcular subtotal
        subtotal = float(precio_unitario * cantidad_comprada)
        # calcular descuento
        descuento = calcular_descuento(subtotal)
        # calcular total
        total_pago = subtotal - descuento

        #### SALIDA
        mostrar_resultado(nombre_producto,subtotal,descuento,total_pago)

        # condicion de cierre
        while True:
            condicion = str(input("¿Desea realizar otra venta (s/n)?: "))
            
            if condicion in("n","N"):
                print("Programa finalizado.")
                cond = False
                break
            elif condicion in("s","S"):
                break
            else:
                print("Opcion ingresada no es valida.")




