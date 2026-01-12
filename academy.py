from utils import somar, subtrair, multiplicar

def main():
    print("Calculadora Simples !")
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    print(f"Soma: {somar(a, b)}")
    print(f"Subtração: {subtrair(a, b)}")
    print(f"multiplaicar: {multiplicar(a, b)}")

if __name__ == "__main__":
    main()