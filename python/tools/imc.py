while True:
    a = input("Insira seu peso:")
    b = input("Insira sua altura:")
    a = float(a)
    b = float(b)

    try:
        print("Seu IMC é:", (a/(b*b)))    
    except ZeroDivisionError:
        print("Números inválidos")
    if (a/(b*b)) <= 18.5:
        print("Magreza")
    elif (a/(b*b)) >= 18.5 and (a/(b*b)) <= 24.9:
        print("Normal")
    elif (a/(b*b)) >= 25 and (a/(b*b)) <= 29.9:
        print("Sobrepeso")
    elif (a/(b*b)) >= 30 and (a/(b*b)) <= 39.9:
        print("Obesidade")
    else:
        print("Obesidade Grave")
