# Entrada e saída
# Exercício 1:
USER_NAME = input("Digite seu nome: ")
for letter in USER_NAME:
    print(letter)

# Exercício 2:
nums = input("Insira valores aqui, separados por espaço: ")

nums_arr = nums.split(" ")

sum = 0
for num in nums_arr:
    if not num.isdigit():
        print(f"Erro ao somar valores, {num} não é um dígito.")
    else:
        sum += int(num)

print(f"A soma dos valores válidos é: {sum}")

# Lidando com exceções
# Exercício 3:
recuperacao = []

with open("alunos_notas.txt", "r") as notas:
    for linha in notas:
        aluno = linha
        aluno = aluno.split(" ")
        if int(aluno[1]) < 6:
            recuperacao.append(aluno[0] + "\n")

with open("alunos_rec.txt", "w") as rec:
    print(recuperacao)
    rec.writelines(recuperacao)
