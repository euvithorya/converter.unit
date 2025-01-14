def metros_para_km(metros):
    return metros / 1000

def metros_para_cm(metros):
    return metros * 100

def metros_para_milhas(metros):
    return metros / 1609.34

def kg_para_gramas(kg):
    return kg * 1000

def kg_para_libras(kg):
    return kg * 2.20462

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def mostrar_menu():
    print("Selecione o tipo de conversão:")
    print("1 - Comprimento")
    print("2 - Peso")
    print("3 - Temperatura")
    print("s - Sair")

def conversor_de_unidades():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção (1/2/3) ou 's' para sair: ")

        if escolha == 's':
            print("Encerrando o conversor de unidades.")
            break

        if escolha == '1':  #-Comprimento
            metros = float(input("Digite o valor em metros: "))
            print(f"{metros} metros é igual a {metros_para_km(metros)} quilômetros.")
            print(f"{metros} metros é igual a {metros_para_cm(metros)} centímetros.")
            print(f"{metros} metros é igual a {metros_para_milhas(metros):.5f} milhas.")

        elif escolha == '2':  #-Peso
            kg = float(input("Digite o valor em quilogramas: "))
            print(f"{kg} quilogramas é igual a {kg_para_gramas(kg)} gramas.")
            print(f"{kg} quilogramas é igual a {kg_para_libras(kg):.5f} libras.")

        elif escolha == '3':  #-Temperatura
            celsius = float(input("Digite o valor em graus Celsius: "))
            print(f"{celsius} °C é igual a {celsius_para_fahrenheit(celsius):.2f} °F.")
            print(f"{celsius} °C é igual a {celsius_para_kelvin(celsius):.2f} K.")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    conversor_de_unidades()

#:P
