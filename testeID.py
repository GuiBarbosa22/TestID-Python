def determinar_categoria(idade, genero):
    if genero == 'M' and idade >= 65:
        return "APOSENTADO"
    elif genero == 'F' and idade >= 60:
        return "APOSENTADA"
    elif 13 <= idade <= 18:
        return "ADOLESCENTE"
    elif idade < 13:
        return "CRIANÇA"
    else:
        return "ADULTO"

def validar_idade(idade):
    if idade <= 0:
        return False
    elif idade > 120:
        return False
    else:
        return True
while True:
    try:
        idade = int(input("Digite a sua idade: "))
        if not validar_idade(idade):
            print("Por favor, insira uma idade válida entre 1 e 120.")
            continue
        break
    except ValueError:
        print("Por favor, insira um número válido para a idade.")

genero = input("Digite o seu gênero (M para masculino, F para feminino): ").upper()

if genero not in ['M', 'F']:
    print("Por favor, insira um gênero válido (M para masculino, F para feminino).")
else:
    categoria = determinar_categoria(idade, genero)
    print(f"Você é classificado como: {categoria}") 