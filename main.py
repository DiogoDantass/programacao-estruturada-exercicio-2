def q1():
    """
    Faça um programa que calcula a
    quantidade de divisores de um
    número (incluindo 1 e o próprio 
    número) que são divisíveis por 3.
    """
    numero = int(input(""))
    quantidade_divisores = 0
    for i in range(2, numero+1):
        if numero % i == 0 and i % 3 == 0:
            quantidade_divisores += 1
    if quantidade_divisores == 0:
        print("O número não possui divisores multiplos de 3")
    else:
        print(
            f"Quantidade de divisores divisiveis por 3: {quantidade_divisores}")

def q2():

    num1 = int(input)("Digite o 1 numero:") # 10
    num2 = int(input)("Digite o 2 numero:") # 5

    # 5 < 10
    if num1 < num2:
        temp = num1 
        num1 = num2
        num2 = temp 

    soma = 0
    for i in range(num1,num2):
        if i > 0:
            soma += i
    print(soma)















def q3():
    """   
    Um professor precisa saber qual a média das notas de uma sala e pediu sua ajuda para construir um programa
    que permita inserir as notas finais de cada aluno e, ao final, exibir a média da sala.
    Lembre-se que as notas variam de 0 a 10 e o professor digitará -1 quando quiser encerrar as entradas.
    Obs.: use variáveis de ponto flutuante de dupla precisão. 
    """
    soma, nota = 0, 0
    while true:
        nota = int(input("Digite uma nota: "))
        if nota == -1:
            break

        if nota in range(0,11):
          soma += nota
           qnt += 1
        
        else:
        print("Valor da nota esta fora do intervalo")

        qnt += 1
     media = soma / qnt
     print(f"A media das notas foi(media)")