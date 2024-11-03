import random
import ast

def detectarRepetidos(legajo, lista):
    return legajo in lista

def escribirDocumento(lista):
    with open("vendedores.txt", "wt") as archivo:
        for credencial in lista:
            archivo.write(credencial + "\n")

def ingresoCredenciales(lista):
    while True:
        try:
            credencial = input("Ingrese una credencial de 5 dígitos (-1 para finalizar): ").strip()
            if credencial == str(-1):
                if len(lista) < 6:
                    print(f"Debes ingresar minimo 6 credenciales. Usted cuenta unicamente con {len(lista)} credencial/es")
                    continue
                break
            if len(credencial) == 5 and credencial.isdigit() and int(credencial) != 0:
                if not detectarRepetidos(credencial, lista):
                    lista.append(credencial)
                else:
                    print("Esta credencial ya fue registrada. Ingrese una nueva")
            else:
                print("Por favor ingrese una credencial de exactamente 5 dígitos.")
        except OSError as msg:
            print("ERROR DE ARCHIVO:", msg)
    escribirDocumento(lista)


def repartirTrabajadores(lista, sedes):
    try:
        with open("sedesArchivadas.txt", "wt") as documentoSedes:
            listaSedes = [[sede] for sede in sedes]
            asignadas = random.sample(lista, len(sedes))
            for i in range(len(sedes)):
                listaSedes[i].append(asignadas[i])
            for credencial in asignadas:
                lista.remove(credencial)
            while lista:
                sedeRandom = random.choice(sedes)
                indiceSede = sedes.index(sedeRandom)
                credencialRandom = random.choice(lista)
                listaSedes[indiceSede].append(credencialRandom)
                lista.remove(credencialRandom)
            for sede in listaSedes:
                documentoSedes.write(str(sede) + "\n")
    except OSError as msg:
        print("ERROR DE ARCHIVO:", msg)


def sumaListaRecursiva(lista):
    if not lista:
        return 0
    return lista[0] + sumaListaRecursiva(lista[1:])


def ventas():
    ventasvendedor = {}
    try:
        with open("VentasSemanales.txt", "wt") as documentoSemanal, open("vendedores.txt", "rt") as documentoCredenciales:
            for linea in documentoCredenciales:
                credencial = linea.strip()
                semana = [random.randint(0, 20) for _ in range(4)]
                totalMes = sumaListaRecursiva(semana)
                
                datos_vendedor = [credencial] + semana + [totalMes]
                
                documentoSemanal.write(str(datos_vendedor) + "\n")

                ventasvendedor[credencial] = semana

    except OSError as msg:
        print("ERROR DE ARCHIVO:", msg)

    return ventasvendedor


def porcentajessemanal(ventasvendedor):
    porcentajefinal = {}
    semanas_totales = [0, 0, 0, 0]
    print(ventasvendedor)

    with open("porcentaje_semanal.txt", "wt") as archivo:
        archivo.write("Porcentaje de ventas por vendedor cada semana: {\n")

        for idx, (credencial, ventas) in enumerate(ventasvendedor.items()):
            total_mes = sum(ventas)
            porcentajes_semanales = {}

            for i, venta_semanal in enumerate(ventas):
                semanas_totales[i] += venta_semanal
                porcentaje = round((venta_semanal / total_mes) * 100, 2) if total_mes > 0 else 0
                semana_key = f"semana{i + 1}"
                porcentajes_semanales[semana_key] = f"{porcentaje} %"

            porcentajefinal[credencial] = porcentajes_semanales

            archivo.write(f"{credencial}: {porcentajes_semanales},\n")

        archivo.write("}\n\n")

        total_mes_general = sum(semanas_totales)
        porcentajes_semanales_totales = {}

        archivo.write("Porcentaje de ventas totales por semana:\n{\n")
        for i, semana_total in enumerate(semanas_totales):
            porcentaje_total_semana = round((semana_total / total_mes_general) * 100, 2) if total_mes_general > 0 else 0
            semana_key = f"semana{i + 1}"
            porcentajes_semanales_totales[semana_key] = f"{porcentaje_total_semana} %"
            archivo.write(f"{semana_key}: {porcentajes_semanales_totales[semana_key]}")
            archivo.write(",\n" if i < len(semanas_totales) - 1 else "\n")

        archivo.write("}\n")

    return porcentajefinal


def porcentajes(total, parte):
    return (parte / total) * 100 if total > 0 else 0


def porcentajeVendedor():
    try:
        with open("PorcentajePorVendedor.txt", "wt") as archSalida1, open("sedesArchivadas.txt", "rt") as documentoSedes, open("VentasSemanales.txt", "rt") as documentoSemanal:
            ventas = {}
            for linea in documentoSemanal:
                try:
                    datos = ast.literal_eval(linea.strip())
                    credencial = datos[0].strip(' "')
                    totalMes = int(datos[-1])
                    ventas[credencial] = totalMes
                except (ValueError, SyntaxError) as e:
                    print(f"Error al interpretar la línea {linea}: {e}")

            sedes = {}
            for linea in documentoSedes:
                try:
                    datos = ast.literal_eval(linea.strip())
                    sede = datos[0]
                    credencialesSede = [cred.strip() for cred in datos[1:]]
                    sedes[sede] = credencialesSede
                except (ValueError, SyntaxError) as e:
                    print(f"Error al interpretar la línea {linea}: {e}")

            resultado = {}
            for sede, vendedores in sedes.items():
                totalSede = sum(ventas.get(cred, 0) for cred in vendedores)
                resultado[sede] = {}
                for vendedor in vendedores:
                    if vendedor in ventas:
                        porcentaje = porcentajes(totalSede, ventas[vendedor])
                        resultado[sede][vendedor] = porcentaje

            for sede, vendedores in resultado.items():
                archSalida1.write(f".Sede: {sede}:\n")
                for vendedor, porcentaje in vendedores.items():
                    archSalida1.write(f"{'Vendedor'.rjust(15)} {vendedor}: {porcentaje:.2f}%\n")
    except OSError as msg:
        print("ERROR DE ARCHIVO:", msg)
    except ValueError as e:
        print("Error al convertir a entero:", e)


def importeTotalSede(precio):
    try:
        with open("Total_por_sede.txt", "wt") as archSalida2, open("VentasSemanales.txt", "rt") as documentoSemana1, open("sedesArchivadas.txt", "rt") as documentosSedes:
            ventas = {}
            for renglón in documentoSemana1:
                partes = renglón.strip().strip("[]()").split(",")
                credencial = partes[0].strip(' "')
                totalMes = int(partes[-1].strip(" )("))
                ventas[credencial] = totalMes

            sedes = {}
            for linea in documentosSedes:
                partes = linea.strip().strip("[]()").split(",")
                sede = partes[0].strip(' "')
                credenciales = [cred.strip() for cred in partes[1:]]
                sedes[sede] = credenciales

            for sede, credenciales in sedes.items():
                total_sede = sum(ventas.get(cred, 0) for cred in credenciales)
                importe = total_sede * precio
                archSalida2.write(f"{sede}= Total de ventas: {importe}$\n")
    except OSError as msg:
        print("ERROR DE ARCHIVO:", msg)
    except ValueError as e:
        print("Error al convertir a entero:", e)



def main():
    COSTO = 500
    listaCredenciales = []
    listaSedes = ["Quilmes", "Sarandi", "Wilde", "Bernal", "V.Dominico", "Ezpeleta"]
    
    ingresoCredenciales(listaCredenciales)
    if listaCredenciales:
        repartirTrabajadores(listaCredenciales, listaSedes)
        ventas_data = ventas()
        porcentajessemanal(ventas_data)
        porcentajeVendedor()
        importeTotalSede(COSTO)
    else:
        print("No se ingresaron datos. No se puede realizar ningún informe")


if __name__ == "__main__":
    main()
