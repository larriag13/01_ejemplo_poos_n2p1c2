from paciente import Paciente

def main():
    # Crear paciente con el constructor __init__
    p1 = Paciente("11.111.111-1", "Luis Arriagada", 40, "Isapre")
    # Mostrar información del paciente
    # __str__ es llamado automáticamente al imprimir el objeto
    print(p1)

if __name__ == "__main__":
    main()  