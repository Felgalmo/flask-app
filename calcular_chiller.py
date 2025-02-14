# Programa para calcular la capacidad de un chiller

def calcular_capacidad_chiller(ce, q, te, ts):
    # Fórmula para calcular la capacidad del chiller
    capacidad = 1000 * ce * q * (te - ts)
    return capacidad

def main():
    print("\nCalculadora de Capacidad de Chiller")
    
    # Solicitar datos al usuario
    try:
        ce = float(input("Ingrese el calor específico del agua (Ce) en kJ/(kg·°C): "))
        q = float(input("Ingrese el caudal de agua del chiller (Q) en m³/h: "))
        te = float(input("Ingrese la temperatura de entrada del agua (Te) en °C: "))
        ts = float(input("Ingrese la temperatura de salida del agua (Ts) en °C: "))

        # Calcular la capacidad del chiller
        capacidad = calcular_capacidad_chiller(ce, q, te, ts)

        # Mostrar el resultado
        print(f"\nLa capacidad del chiller es: {capacidad:.2f} kW")
    except ValueError:
        print("Error: Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()
