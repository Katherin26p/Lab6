import matplotlib.pyplot as plt
import mplcursors

def main():
    print("Bienvenido al Laboratorio de Suma Acumulativa")

    numero = int(input("Ingrese la cantidad de números que desea sumar: "))

    if numero <= 0:
        print("Ingrese un número entero positivo.")
        return

    numbers = []
    cumulative_sum = 0
    cumulative_sums = []

    for i in range(numero):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                break
            except ValueError:
                print("Ingrese un número válido.")

        cumulative_sum += num
        numbers.append(num)
        cumulative_sums.append(cumulative_sum)
    print("Suma acumulativa de los números ingresados:")
    for i, total in enumerate(cumulative_sums):
        print(f"Número {i+1}: {total}")

    plt.plot(range(1, numero+1), cumulative_sums, marker='o', color='purple')
    plt.xlabel("Número de entrada")
    plt.ylabel("Suma acumulativa")
    plt.title("Gráfico de Suma Acumulativa (Curvas)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
