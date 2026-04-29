
import random

# --- Función para llenar automáticamente la matriz ---
def llenar_matriz_automatica():
    matriz = []
    codigos = [1015, 1030, 1045]  # Fútbol, Basketball, Ciclismo
    for i in range(100):
        cedula = random.randint(10000000, 99999999)   # Cédula aleatoria
        sexo = random.choice([1, 2])                  # 1 = Mujer, 2 = Hombre
        edad = random.randint(18, 30)                 # Edad entre 18 y 30 años
        codigo = random.choice(codigos)               # Selección aleatoria
        matriz.append([cedula, sexo, edad, codigo])
    return matriz


# --- Función para mostrar la matriz ---
def mostrar_matriz(matriz):
    print("\n=== MATRIZ DE DEPORTISTAS ===")
    print("Cédula\t\tSexo\tEdad\tSelección")
    for fila in matriz:
        sexo_str = "Mujer" if fila[1] == 1 else "Hombre"
        print(f"{fila[0]}\t{sexo_str}\t{fila[2]}\t{fila[3]}")


# --- Función para calcular porcentaje de hombres y mujeres ---
def porcentaje_sexo(matriz):
    total = len(matriz)
    mujeres = sum(1 for fila in matriz if fila[1] == 1)
    hombres = total - mujeres

    porc_mujeres = (mujeres / total) * 100
    porc_hombres = (hombres / total) * 100

    print("\n=== PORCENTAJE POR SEXO ===")
    print(f"Mujeres: {porc_mujeres:.2f}%")
    print(f"Hombres: {porc_hombres:.2f}%")


# --- Función para contar deportistas por selección ---
def deportistas_por_seleccion(matriz):
    futbol = sum(1 for fila in matriz if fila[3] == 1015)
    basket = sum(1 for fila in matriz if fila[3] == 1030)
    ciclismo = sum(1 for fila in matriz if fila[3] == 1045)

    print("\n=== DEPORTISTAS POR SELECCIÓN ===")
    print(f"Fútbol: {futbol}")
    print(f"Basketball: {basket}")
    print(f"Ciclismo: {ciclismo}")


# --- PROGRAMA PRINCIPAL ---
def main():
    matriz = llenar_matriz_automatica()
    mostrar_matriz(matriz)
    porcentaje_sexo(matriz)
    deportistas_por_seleccion(matriz)


# --- Ejecutar ---
if __name__ == "__main__":
    main()

